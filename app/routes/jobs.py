from fastapi import APIRouter

from ..scrapers.greenhouse import scrape_greenhouse
from ..scrapers.lever import scrape_lever

router = APIRouter()


@router.get("/jobs/scrape")
def scrape_jobs():
    jobs = []
    jobs += scrape_greenhouse("openai")
    jobs += scrape_lever("stripe")
    return jobs
