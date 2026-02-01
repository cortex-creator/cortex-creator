import httpx
from bs4 import BeautifulSoup


def scrape_greenhouse(company: str):
    url = f"https://boards.greenhouse.io/{company}"
    jobs = []

    r = httpx.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    for a in soup.select("a[href*='/jobs/']"):
        jobs.append(
            {
                "title": a.text.strip(),
                "url": "https://boards.greenhouse.io" + a["href"],
                "company": company,
                "location": "Remote",
                "source": "greenhouse",
                "description": "",
            }
        )

    return jobs
