def parse_product(crawl_result : dict) ->dict:

    markdown = crawl_result.get("markdown") or ""
    metadata = crawl_result.get("metadata") or {}

    lines = [line.strip() for line in markdown.splitlines() if line.strip()]

    name = metadata.get("title")

    if not name and lines:
        name = lines[0].lstrip("#").strip()

    return {
        "name" : name,
        "price": find_value(lines , "price"),
        "rating" : find_value(lines , "rating"),
        "availability": find_value(lines , "availability"),
        "url" : crawl_result.get("url"),

    }


def find_value(lines: list[str] , keyword: str):
    for line in lines:
        if keyword.lower() in line.lower():
            return line.split(":" , 1)[-1].strip()

    return None