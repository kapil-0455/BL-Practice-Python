from src.processing.normalizer import normalize_product
from src.processing.parser import parse_product


def test_parser():

    crawl_result = {
        "url": "https://example.com/product",
        "markdown": """
        # Boat Headphones

        Price: ₹1,499

        Rating: 4.5

        Availability: In Stock
        """,
        "metadata": {"title": "Boat Headphones"},
    }

    result = parse_product(crawl_result)

    assert result["name"] == "Boat Headphones"
    assert result["price"] == "₹1,499"
    assert result["rating"] == "4.5"
    assert result["availability"] == "In Stock"
    assert result["url"] == "https://example.com/product"


def test_normalization():

    product = {
        "name": "  Boat Headphones  ",
        "price": " ₹1,499 ",
        "rating": "4.5",
        "availability": " In Stock ",
        "url": " https://example.com/product ",
    }

    result = normalize_product(product)

    assert result["name"] == "Boat Headphones"
    assert result["price"] == "₹1,499"
    assert result["rating"] == "4.5"
    assert result["availability"] == "In Stock"
    assert result["url"] == "https://example.com/product"
