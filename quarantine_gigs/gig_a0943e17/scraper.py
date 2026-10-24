#!/usr/bin/env python3
"""Polite web scraper."""

import argparse
import csv
import os
import sys
import time
import urllib.request
import urllib.robotparser
import urllib.parse
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []  # list of dicts with href and text
        self.title = None
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            href = dict(attrs).get('href')
            if href:
                self.links.append({'href': href, 'text': ''})
        elif tag == 'title':
            self._in_title = True

    def handle_data(self, data):
        if self._in_title:
            self.title = data
            self._in_title = False

    def handle_endtag(self, tag):
        if tag == 'title':
            self._in_title = False

class PoliteScraper:
    def __init__(self, delay=1, respect_robots=True, output_file='results.csv'):
        self.delay = delay
        self.respect_robots = respect_robots
        self.output_file = output_file
        self.seen_urls = set()
        self.rp = urllib.robotparser.RobotFileParser()
        self.rp_parsed = False

    def can_fetch(self, url):
        if not self.respect_robots:
            return True
        # We need to fetch robots.txt if not already done
        # But robots.txt is per domain, so we should cache per domain.
        # For simplicity, we can parse robots.txt on first request to a domain.
        parsed = urlparse(url)
        base = f"{parsed.scheme}://{parsed.netloc}"
        robots_url = urljoin(base, 'robots.txt')
        # Check if we have already parsed robots.txt for this domain
        if not hasattr(self, '_robots_cache'):
            self._robots_cache = {}
        if base not in self._robots_cache:
            try:
                self.rp = urllib.robotparser.RobotFileParser()
                self.rp.set_url(robots_url)
                self.rp.read()
                self._robots_cache[base] = self.rp
            except Exception:
                # If robots.txt cannot be fetched, assume allowed
                self._robots_cache[base] = None
        rp = self._robots_cache[base]
        if rp is None:
            return True
        return rp.can_fetch('*', url)

    def fetch(self, url):
        # Check if already seen
        if url in self.seen_urls:
            return None
        # Check robots.txt
        if not self.can_fetch(url):
            print(f"Disallowed by robots.txt: {url}", file=sys.stderr)
            return None
        # Fetch
        try:
            with urllib.request.urlopen(url) as response:
                html = response.read().decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"Error fetching {url}: {e}", file=sys.stderr)
            return None
        # Add to seen
        self.seen_urls.add(url)
        # Sleep for crawl delay
        time.sleep(self.delay)
        return html

    def parse(self, html, url):
        extractor = LinkExtractor()
        extractor.feed(html)
        title = extractor.title
        links = extractor.links
        # Resolve relative links
        for link in links:
            link['href'] = urljoin(url, link['href'])
        return title, links

    def save_to_csv(self, url, title, links):
        # Append to CSV
        file_exists = os.path.isfile(self.output_file)
        with open(self.output_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(['url', 'title', 'link_href', 'link_text'])
            for link in links:
                writer.writerow([url, title, link['href'], link['text']])

    def scrape(self, start_url):
        html = self.fetch(start_url)
        if html is None:
            return
        title, links = self.parse(html, start_url)
        self.save_to_csv(start_url, title, links)
        # Optionally follow links? The brief says "extracts article titles and links", not necessarily crawl. But it's a scraper CLI, maybe just scrape the given URL. However, it says "web scraper" and "crawl delay", so maybe it should crawl. But the brief doesn't explicitly say to follow links. It says "fetches pages with urllib, respects a configurable crawl delay and robots.txt disallow rules, extracts article titles and links via html.parser, and appends results to a CSV with deduplication by URL." It doesn't say to recursively crawl. So likely it's a single-page scraper. But the mention of "crawl delay" implies it might be used for multiple pages. The CLI could accept multiple URLs. Let's design it to accept one or more URLs as arguments and scrape each.

def main():
    parser = argparse.ArgumentParser(description='Polite web scraper')
    parser.add_argument('urls', nargs='+', help='URLs to scrape')
    parser.add_argument('-o', '--output', default='results.csv', help='Output CSV file')
    parser.add_argument('-d', '--delay', type=float, default=1.0, help='Crawl delay in seconds')
    parser.add_argument('--no-robots', action='store_true', help='Ignore robots.txt')
    args = parser.parse_args()
    scraper = PoliteScraper(delay=args.delay, respect_robots=not args.no_robots, output_file=args.output)
    for url in args.urls:
        scraper.scrape(url)

if __name__ == '__main__':
    main()