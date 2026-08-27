import pytest

from src.http.httpx_client import async_fetch, async_fetch_many

PRODUCT_URLS = [
    "https://www.boat-lifestyle.com/products/nirvana-ion-bluetooth-wireless-earbuds",
    "https://www.gonoise.com/products/noise-air-buds-truly-wireless-earbuds",
    "https://www.themancompany.com/products/all-about-him",
]


@pytest.mark.asyncio
async def test_async_request():

    result = await async_fetch(PRODUCT_URLS[0])

    assert result["success"] is True
    assert result["status_code"] == 200
    assert result["content"] is not None


@pytest.mark.asyncio
async def test_async_multiple_requests():

    results = await async_fetch_many(PRODUCT_URLS)

    assert len(results) == 3

    for result in results:
        assert result["success"] is True
        assert result["status_code"] == 200


@pytest.mark.asyncio
async def test_http_error():

    result = await async_fetch("https://httpbin.org/status/404")

    assert result["success"] is False
    assert result["status_code"] == 404
    assert result["error"] == "HTTP 404"
