from crawl4ai import AsyncWebCrawler


async def crawl_page(url: str) -> dict:

    try:
        async with AsyncWebCrawler() as crawler:
            result = await crawler.arun(url=url)

            return {
                "url": url,
                "html": result.html,
                "markdown": result.markdown,
                "links": result.links,
                "metadata": result.metadata,
                "success": True,
                "error": None,
            }
    except Exception as exc:  
        return {
            "url": url,
            "html": None,
            "markdown": None,
            "links": {},
            "metadata": {},
            "success": False,
            "error": str(exc),
        }
