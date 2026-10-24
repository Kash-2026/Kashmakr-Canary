import csv
import time
import urllib.request
import urllib.parse
import urllib.robotparser
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.titles = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            href = dict(attrs).get("href")
            if href:
                self.links.append(href)
        elif tag == "title":
            self.titles.append("")

    def handle_data(self, data):
        if self.titles and self.titles[-1] == "":
            self.titles[-1] = data


def fetch_url(url, delay, user_agent, rp):
    if not rp.can_fetch(user_agent, url):
        return None
    parsed_url = urllib.parse.urlparse(url)
    with urllib.request.urlopen(url) as response:
        html_content = response.read().decode("utf-8")
    parser = MyHTMLParser()
    parser.feed(html_content)
    time.sleep(delay)
    return parser.titles, parser.links


def write_to_csv(file_path, url, title, link):
    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([url, title, link])


def scrape(start_url, output_csv, delay, user_agent):
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(urllib.parse.urljoin(start_url, "/robots.txt"))
    rp.read()

    visited_urls = set()
    with open(output_csv, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["URL", "Title", "Link"])

    queue = [start_url]
    while queue:
        current_url = queue.pop(0)
        if current_url in visited_urls:
            continue
        visited_urls.add(current_url)
        titles, links = fetch_url(current_url, delay, user_agent, rp)
        if titles and links:
            for title, link in zip(titles, links):
                full_url = urllib.parse.urljoin(current_url, link)
                if full_url not in visited_urls:
                    write_to_csv(output_csv, current_url, title, full_url)
                    queue.append(full_url)
