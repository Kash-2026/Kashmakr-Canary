import asyncio
from datetime import datetime, timedelta
from typing import Any, Callable, Dict, Optional


class AsyncFetchCache:
    def __init__(self, fetch_function: Callable[[str], asyncio.Future], ttl: timedelta):
        self.fetch_function = fetch_function
        self.ttl = ttl
        self.cache: Dict[str, Any] = {}
        self.cache_expiry: Dict[str, datetime] = {}
        self.in_flight: Dict[str, asyncio.Future] = {}

    async def fetch(self, key: str) -> Optional[Any]:
        if key in self.cache and self.cache_expiry[key] > datetime.now():
            return self.cache[key]
        if key in self.in_flight:
            return await self.in_flight[key]

        future = self.fetch_function(key)
        self.in_flight[key] = future
        try:
            result = await future
            self.cache[key] = result
            self.cache_expiry[key] = datetime.now() + self.ttl
            return result
        except Exception as e:
            raise e
        finally:
            del self.in_flight[key]

    async def clear(self, key: str):
        if key in self.cache:
            del self.cache[key]
        if key in self.cache_expiry:
            del self.cache_expiry[key]
        if key in self.in_flight:
            del self.in_flight[key]
