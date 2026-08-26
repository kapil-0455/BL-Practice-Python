import asyncio
import time

import httpx

DEFAULT_TIMEOUT = 10
MAX_RETRIES = 3


async def async_fetch(url: str) -> dict:
    timeout = httpx.Timeout(DEFAULT_TIMEOUT)

    async with httpx.AsyncClient(timeout=timeout) as client:
        for attempt in range(MAX_RETRIES + 1):
            try:
                start = time.perf_counter()

                response = await client.get(url)

                end = time.perf_counter()

                completion_time = end - start

                # 2xx => success
                if 200 <= response.status_code < 300:
                    return {
                        "url": url,
                        "status_code": response.status_code,
                        "content": response.text,
                        "headers": dict(response.headers),
                        "elapsed": completion_time,
                        "success": True,
                        "error": None,
                    }

                # 4xx => don't blindly retry
                if 400 <= response.status_code < 500:
                    return {
                        "url": url,
                        "status_code": response.status_code,
                        "content": response.text,
                        "headers": dict(response.headers),
                        "elapsed": completion_time,
                        "success": False,
                        "error": f"HTTP {response.status_code}",
                    }

                # 5xx => retry
                if 500 <= response.status_code < 600:
                    if attempt < MAX_RETRIES:
                        continue

                    return {
                        "url": url,
                        "status_code": response.status_code,
                        "content": response.text,
                        "headers": dict(response.headers),
                        "elapsed": completion_time,
                        "success": False,
                        "error": f"HTTP {response.status_code} after retries",
                    }

            except httpx.TimeoutException:
                if attempt < MAX_RETRIES:
                    continue

                return {
                    "url": url,
                    "status_code": None,
                    "content": None,
                    "headers": {},
                    "elapsed": None,
                    "success": False,
                    "error": "Request timeout",
                }

            except httpx.ConnectError:
                if attempt < MAX_RETRIES:
                    continue

                return {
                    "url": url,
                    "status_code": None,
                    "content": None,
                    "headers": {},
                    "elapsed": None,
                    "success": False,
                    "error": "Connection error",
                }

            except httpx.RequestError as exc:
                return {
                    "url": url,
                    "status_code": None,
                    "content": None,
                    "headers": {},
                    "elapsed": None,
                    "success": False,
                    "error": str(exc),
                }

    return {
        "url": url,
        "status_code": None,
        "content": None,
        "headers": {},
        "elapsed": None,
        "success": False,
        "error": "Unknown request failure",
    }


async def async_fetch_many(urls: list[str]) -> list[dict]:

    tasks = [async_fetch(url) for url in urls]
    return await asyncio.gather(*tasks)
