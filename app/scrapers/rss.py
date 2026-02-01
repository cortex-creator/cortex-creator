import feedparser


def scrape_rss(feed_url: str):
    feed = feedparser.parse(feed_url)
    jobs = []

    for entry in feed.entries:
        jobs.append(
            {
                "title": entry.title,
                "url": entry.link,
                "company": "RSS",
                "location": "Remote",
                "source": "rss",
                "description": entry.get("summary", ""),
            }
        )

    return jobs
