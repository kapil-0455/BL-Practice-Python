def normalize_product(product: dict) -> dict:
    return {
        "name": clean(product.get("name")),
        "price": clean(product.get("price")),
        "rating": clean(product.get("rating")),
        "availability": clean(product.get("availability")),
        "url": clean(product.get("url")),
    }


def clean(value):
    if value is None:
        return None

    value = str(value).strip()

    return value if value else None