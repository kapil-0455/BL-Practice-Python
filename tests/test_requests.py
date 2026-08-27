import pytest

from src.http.requests_client import fetch_page

PRODUCT_URLS = [
    "https://www.boat-lifestyle.com/products/nirvana-ion-bluetooth-wireless-earbuds",
    "https://www.gonoise.com/products/noise-air-buds-truly-wireless-earbuds",
    "https://www.themancompany.com/products/all-about-him",
]


@pytest.mark.parametrize("url", PRODUCT_URLS)
def test_successful_product_request(url):

    result = fetch_page(url)

    assert result["success"] is True
    assert result["status_code"] == 200
    assert result["content"] is not None
    assert len(result["content"]) > 0
    assert result["url"] == url


def test_invalid_url():

    result = fetch_page("https://this-domain-does-not-exist-123456789.com")

    assert result["success"] is False
    assert result["error"] == "Connection error"


def test_timeout():

    result = fetch_page("https://httpbin.org/delay/20")

    assert result["success"] is False
    assert result["error"] == "Request timeout"
