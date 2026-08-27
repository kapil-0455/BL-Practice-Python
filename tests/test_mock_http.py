from unittest.mock import AsyncMock, Mock, patch

import pytest

from src.http.httpx_client import async_fetch
from src.http.requests_client import fetch_page


def test_requests_mock():

    response = Mock()
    response.status_code = 200
    response.text = "Mock Product"
    response.headers = {}

    with patch("src.http.requests_client.requests.get", return_value=response):
        result = fetch_page("https://real-website.com/product")

    assert result["success"] is True
    assert result["status_code"] == 200
    assert result["content"] == "Mock Product"


@pytest.mark.asyncio
async def test_httpx_mock():

    response = Mock()
    response.status_code = 200
    response.text = "Mock Product"
    response.headers = {}

    client = AsyncMock()
    client.get.return_value = response

    with patch("src.http.httpx_client.httpx.AsyncClient") as mock_client:
        mock_client.return_value.__aenter__.return_value = client

        result = await async_fetch("https://real-website.com/product")

    assert result["success"] is True
    assert result["status_code"] == 200
    assert result["content"] == "Mock Product"
