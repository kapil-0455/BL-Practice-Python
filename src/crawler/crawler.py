from crawl4ai import AsyncWebCrawler


async def crawl_page(url: str) -> dict:

    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url=url)

    return {
        "url": url,
        "html": result.html,
        "markdown": result.markdown,
        "links": result.links,
        "metadata": result.metadata,
    }
