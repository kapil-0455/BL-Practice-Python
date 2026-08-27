import logging
import time

from src.http.httpx_client import async_fetch_many
from src.http.requests_client import fetch_page

logging.basicConfig(level=logging.INFO, format="%(message)s")


def fetch_sequential(urls: list[str]) -> dict:

    start_time = time.perf_counter()
    results = []

    for url in urls:
        res = fetch_page(url)
        results.append(res)

    end_time = time.perf_counter()

    completion_time = end_time - start_time

    return {"results": results, "elapsed": completion_time}


async def fetch_concurrent(urls: list[str]) -> dict:

    start_time = time.perf_counter()

    result = await async_fetch_many(urls)

    end_time = time.perf_counter()

    completion_time = end_time - start_time

    return {"results": result, "elapsed": completion_time}


def calculate_improvement(sequential_time: float, concurrent_time: float):

    if sequential_time == 0:
        return 0.0

    return ((sequential_time - concurrent_time) / sequential_time) * 100


async def run_benchmark(urls: list[str]) -> dict:

    sequential = fetch_sequential(urls)

    concurrent = await fetch_concurrent(urls)

    improvement = calculate_improvement(sequential["elapsed"], concurrent["elapsed"])

    return {
        "sequential_time": sequential["elapsed"],
        "concurrent_time": concurrent["elapsed"],
        "improvement_percent": improvement,
        "sequential_results": sequential["results"],
        "concurrent_results": concurrent["results"],
    }


def summarize_results(results: list[dict]) -> dict:

    successful = sum(1 for result in results if result["success"])

    failed = len(results) - successful

    return {"total_urls": len(results), "successful": successful, "failed": failed}
