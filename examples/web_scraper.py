# %%

import collections
import requests
import concurrent.futures
import threading
from bs4 import BeautifulSoup
from typing import List, Set
from urllib.parse import urljoin, urlparse

# %%

def get_links(url: str) -> List[str]:
    """Get all the links on a page."""
    page = requests.get(url)
    bs = BeautifulSoup(page.content, features='lxml')
    links = [link.get("href") for link in bs.findAll('a')]
    absolute_urls = [urljoin(url, link) for link in links]
    return absolute_urls

# %%

def has_same_hostname(url: str, other_url: str) -> bool:
    """Check if two URLs have the same hostname."""
    host = urlparse(url).hostname
    other_host = urlparse(other_url).hostname
    return host == other_host

# %%

def threaded_scraper(url: str) -> Set[str]:
    """Scrape a website using multiple threads."""
    visiting = set([url])
    scraped = set()
    scraped_lock = threading.Lock()
    visiting_lock = threading.Lock()
    cv = threading.Condition()
    executor = concurrent.futures.ThreadPoolExecutor()

    def mark_as_visited(link: str) -> None:
        with visiting_lock:
            visiting.remove(link)
        
        with cv:
            cv.notify()
    
    def worker(link: str) -> None:
        if not has_same_hostname(url, link):
            mark_as_visited(link)
            return  # ignore links outside domain

        with scraped_lock:
            if link in scraped:
                mark_as_visited(link)
                return  # don't scrape same link twice

            scraped.add(link)
        
        for child in get_links(link):
            with visiting_lock:
                visiting.add(child)
            
            executor.submit(worker, child)

        mark_as_visited(link)
    
    executor.submit(worker, url)

    with cv:
        cv.wait_for(lambda: len(visiting) == 0)

    executor.shutdown(wait=True, cancel_futures=False)
    
    return scraped


threaded_scraper("https://karpathy.github.io/")

# %%

def non_threaded_scraper(url: str) -> Set[str]:
    """Scrape a website using single thread."""
    q = collections.deque([url])
    seen = set()

    while q:
        link = q.popleft()

        if not has_same_hostname(url, link):
            continue

        if link in seen:
            continue

        seen.add(link)

        for child in get_links(link):
            q.append(child)

    return seen


non_threaded_scraper("https://karpathy.github.io/")

# %%

assert threaded_scraper("https://karpathy.github.io/") == non_threaded_scraper("https://karpathy.github.io/")

# %%
