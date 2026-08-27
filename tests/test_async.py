import asyncio

import pytest

from src.http.httpx_client import async_fetch_many

PRODUCT_URLS = [
    "https://www.boat-lifestyle.com/products/nirvana-ion-bluetooth-wireless-earbuds",
    "https://www.gonoise.com/products/noise-air-buds-truly-wireless-earbuds",
    "https://www.themancompany.com/products/all-about-him",
]


@pytest.mark.asyncio
async def test_concurrent_execution():

    start = asyncio.get_running_loop().time()

    results = await async_fetch_many(PRODUCT_URLS)

    elapsed = asyncio.get_running_loop().time() - start

    assert len(results) == 3
    assert elapsed < 30


@pytest.mark.asyncio
async def test_partial_failure():

    urls = [
        PRODUCT_URLS[0],
        "https://this-domain-does-not-exist-123456789.com",
        PRODUCT_URLS[2],
    ]

    results = await async_fetch_many(urls)

    successful = sum(result["success"] for result in results)

    failed = len(results) - successful

    assert len(results) == 3
    assert successful == 2
    assert failed == 1
