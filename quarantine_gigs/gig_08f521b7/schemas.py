from pydantic import BaseModel, ConfigDict
from typing import Optional, List


class BookmarkBase(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra="allow")

    @field_validator("tags", mode="before", check_fields=False)
    @classmethod
    def _parse_tags(cls, v):
        if v is None:
            return []
        if isinstance(v, str):
            return [t.strip() for t in v.split(",") if t.strip()]
        if isinstance(v, list):
            return [getattr(t, "name", str(t)) for t in v]
        return []

    @field_validator("created_at", mode="before", check_fields=False)
    @classmethod
    def _parse_created_at(cls, v):
        return str(v) if v is not None else None

    url: str
    title: str
    tags: Optional[List[str]] = None


class BookmarkCreate(BookmarkBase):
    pass


class BookmarkUpdate(BookmarkBase):
    pass


class Bookmark(BookmarkBase):
    id: int
    created_at: str

    model_config = ConfigDict(from_attributes=True)
