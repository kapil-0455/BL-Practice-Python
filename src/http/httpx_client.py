import asyncio
import logging
import time

import httpx

CONNECT_TIMEOUT = 5.0
READ_TIMEOUT = 10.0
WRITE_TIMEOUT = 10.0
POOL_TIMEOUT = 5.0

MAX_RETRIES = 3
MAX_CONCURRENT_REQUESTS = 5
RATE_LIMIT  = 1.0


logger = logging.getLogger(__name__)


def retry_delay(attempt: int, base_delay: float = 1.0) -> float:
    return base_delay * (2**attempt)


async def async_fetch(url: str) -> dict:

    timeout = httpx.Timeout(
        connect=CONNECT_TIMEOUT,
        read=READ_TIMEOUT,
        write=WRITE_TIMEOUT,
        pool=POOL_TIMEOUT,
    )

    async with httpx.AsyncClient(timeout=timeout) as client:
        for attempt in range(MAX_RETRIES + 1):
            start = time.perf_counter()

            try:
                response = await client.get(url)

                completion_time = time.perf_counter() - start

                # 2xx => success
                if 200 <= response.status_code < 300:
                    logger.info(
                        "url=%s timestamp=%s status=%s latency=%.3f "
                        "retry_count=%s error=%s",
                        url,
                        time.strftime("%Y-%m-%d %H:%M:%S"),
                        response.status_code,
                        completion_time,
                        attempt,
                        None,
                    )

                    return {
                        "url": url,
                        "status_code": response.status_code,
                        "content": response.text,
                        "headers": dict(response.headers),
                        "elapsed": completion_time,
                        "success": True,
                        "error": None,
                    }

                # 4xx => don't retry
                if 400 <= response.status_code < 500:
                    logger.warning(
                        "url=%s timestamp=%s status=%s latency=%.3f "
                        "retry_count=%s error=%s",
                        url,
                        time.strftime("%Y-%m-%d %H:%M:%S"),
                        response.status_code,
                        completion_time,
                        attempt,
                        f"HTTP {response.status_code}",
                    )

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
                    error = f"HTTP {response.status_code}"

                    if attempt < MAX_RETRIES:
                        logger.warning(
                            "url=%s timestamp=%s status=%s latency=%.3f "
                            "retry_count=%s error=%s",
                            url,
                            time.strftime("%Y-%m-%d %H:%M:%S"),
                            response.status_code,
                            completion_time,
                            attempt,
                            error,
                        )

                        delay = retry_delay(attempt)
                        await asyncio.sleep(delay)
                        continue

                    logger.error(
                        "url=%s timestamp=%s status=%s latency=%.3f "
                        "retry_count=%s error=%s",
                        url,
                        time.strftime("%Y-%m-%d %H:%M:%S"),
                        response.status_code,
                        completion_time,
                        attempt,
                        f"{error} after retries",
                    )

                    return {
                        "url": url,
                        "status_code": response.status_code,
                        "content": response.text,
                        "headers": dict(response.headers),
                        "elapsed": completion_time,
                        "success": False,
                        "error": f"{error} after retries",
                    }

            except httpx.TimeoutException:
                completion_time = time.perf_counter() - start

                if attempt < MAX_RETRIES:
                    logger.warning(
                        "url=%s timestamp=%s status=%s latency=%.3f "
                        "retry_count=%s error=%s",
                        url,
                        time.strftime("%Y-%m-%d %H:%M:%S"),
                        None,
                        completion_time,
                        attempt,
                        "Request timeout",
                    )

                    delay = retry_delay(attempt)
                    await asyncio.sleep(delay)
                    continue

                logger.error(
                    "url=%s timestamp=%s status=%s latency=%.3f "
                    "retry_count=%s error=%s",
                    url,
                    time.strftime("%Y-%m-%d %H:%M:%S"),
                    None,
                    completion_time,
                    attempt,
                    "Request timeout",
                )

                return {
                    "url": url,
                    "status_code": None,
                    "content": None,
                    "headers": {},
                    "elapsed": completion_time,
                    "success": False,
                    "error": "Request timeout",
                }

            except httpx.ConnectError:
                completion_time = time.perf_counter() - start

                if attempt < MAX_RETRIES:
                    logger.warning(
                        "url=%s timestamp=%s status=%s latency=%.3f "
                        "retry_count=%s error=%s",
                        url,
                        time.strftime("%Y-%m-%d %H:%M:%S"),
                        None,
                        completion_time,
                        attempt,
                        "Connection error",
                    )

                    delay = retry_delay(attempt)
                    await asyncio.sleep(delay)
                    continue

                logger.error(
                    "url=%s timestamp=%s status=%s latency=%.3f "
                    "retry_count=%s error=%s",
                    url,
                    time.strftime("%Y-%m-%d %H:%M:%S"),
                    None,
                    completion_time,
                    attempt,
                    "Connection error",
                )

                return {
                    "url": url,
                    "status_code": None,
                    "content": None,
                    "headers": {},
                    "elapsed": completion_time,
                    "success": False,
                    "error": "Connection error",
                }

            except httpx.RequestError as exc:
                completion_time = time.perf_counter() - start

                if attempt < MAX_RETRIES:
                    logger.warning(
                        "url=%s timestamp=%s status=%s latency=%.3f "
                        "retry_count=%s error=%s",
                        url,
                        time.strftime("%Y-%m-%d %H:%M:%S"),
                        None,
                        completion_time,
                        attempt,
                        str(exc),
                    )

                    delay = retry_delay(attempt)
                    await asyncio.sleep(delay)
                    continue

                logger.error(
                    "url=%s timestamp=%s status=%s latency=%.3f "
                    "retry_count=%s error=%s",
                    url,
                    time.strftime("%Y-%m-%d %H:%M:%S"),
                    None,
                    completion_time,
                    attempt,
                    str(exc),
                )

                return {
                    "url": url,
                    "status_code": None,
                    "content": None,
                    "headers": {},
                    "elapsed": completion_time,
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


async def limited_fetch(url: str, semaphore: asyncio.Semaphore) -> dict:

    async with semaphore:
        await asyncio.sleep(RATE_LIMIT)
        return await async_fetch(url)


async def async_fetch_many(urls: list[str]) -> list[dict]:

    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

    tasks = [limited_fetch(url, semaphore) for url in urls]

    return await asyncio.gather(*tasks)
