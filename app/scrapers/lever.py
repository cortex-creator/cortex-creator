import httpx
from bs4 import BeautifulSoup


def scrape_lever(company: str):
    url = f"https://jobs.lever.co/{company}"
    jobs = []

    r = httpx.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    for a in soup.select("a.posting-title"):
        jobs.append(
            {
                "title": a.text.strip(),
                "url": a["href"],
                "company": company,
                "location": "Remote",
                "source": "lever",
                "description": "",
            }
        )

    return jobs
