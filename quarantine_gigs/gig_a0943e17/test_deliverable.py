import csv
import time
import urllib.request
import urllib.parse
import html.parser
import html


class _TitleExtractor(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.titles = []
        self.in_title = False
        self.title_parts = []

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
            title = ''.join(self.title_parts)
            self.titles.append(html.unescape(title))
            self.title_parts = []

    def handle_data(self, data):
        if self.in_title:
            self.title_parts.append(data)


class _LinkExtractor(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, value in attrs:
                if attr == 'href':
                    self.links.append(value)


class PoliteScraper:
    def __init__(self, base_url, crawl_delay, output_csv):
        if not base_url.endswith('/'):
            base_url += '/'
        self.base_url = base_url
        self.crawl_delay = crawl_delay
        self.output_csv = output_csv
        self.visited_urls = set()

    def fetch(self, url):
        time.sleep(self.crawl_delay)
        with urllib.request.urlopen(url) as response:
            return response.read()

    def parse(self, html_content):
        parser = _TitleExtractor()
        parser.feed(html_content.decode())
        return parser.titles

    def extract_links(self, html_content):
        parser = _LinkExtractor()
        parser.feed(html_content.decode())
        return parser.links

    def is_allowed(self, url):
        robots_txt_url = urllib.parse.urljoin(self.base_url, "/robots.txt")
        try:
            with urllib.request.urlopen(robots_txt_url) as response:
                robots_txt = response.read().decode()
                for line in robots_txt.split("\n"):
                    if line.startswith("Disallow:"):
                        parts = line.split(" ", 1)
                        if len(parts) > 1:
                            disallow_path = parts[1].strip()
                            if disallow_path and disallow_path in url:
                                return False
        except urllib.error.HTTPError:
            pass
        return True

    def scrape(self):
        to_visit = [self.base_url]
        with open(self.output_csv, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            while to_visit:
                current_url = to_visit.pop(0)
                if current_url in self.visited_urls:
                    continue
                self.visited_urls.add(current_url)
                if not self.is_allowed(current_url):
                    continue
                html_content = self.fetch(current_url)
                titles = self.parse(html_content)
                links = self.extract_links(html_content)
                writer.writerow([current_url] + titles)
                for link in links:
                    absolute_url = urllib.parse.urljoin(current_url, link)
                    if absolute_url not in self.visited_urls:
                        to_visit.append(absolute_url)