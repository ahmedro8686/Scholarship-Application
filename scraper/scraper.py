import requests
from bs4 import BeautifulSoup
from time import sleep
from config import Config
from database.queries import add_scholarship

HEADERS = {"User-Agent": "Mozilla/5.0"}

def fetch_scholarships(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch {url}")
    
    soup = BeautifulSoup(response.text, "html.parser")
    scholarships = parse_scholarships(soup)
    
    for s in scholarships:
        add_scholarship(s)
        sleep(Config.SCRAPER_DELAY)
    
    return scholarships

def parse_scholarships(soup):
    # Dummy parsing logic — replace with actual selectors
    results = []
    for item in soup.select(".scholarship"):
        results.append({
            "title": item.select_one(".title").text,
            "description": item.select_one(".desc").text,
            "country": item.select_one(".country").text,
            "level": item.select_one(".level").text,
            "deadline": item.select_one(".deadline").text,
            "url": item.select_one("a")["href"]
        })
    return results
