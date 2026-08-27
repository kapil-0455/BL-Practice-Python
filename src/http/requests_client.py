import time

import requests

DEFAULT_TIMEOUT = 10
MAX_RETRIES = 3


def retry_delay(attempt: int, base_delay: float = 1.0) -> float:
    return base_delay * (2**attempt)


def fetch_page(url: str) -> dict:

    for attempt in range(MAX_RETRIES + 1):
        try:
            start_time = time.perf_counter()
            response = requests.get(url,timeout= DEFAULT_TIMEOUT)

            end_time = time.perf_counter()

            completion_time = end_time - start_time

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

            if 500 <= response.status_code < 600:
                if attempt < MAX_RETRIES:
                    delay = 2**attempt
                    time.sleep(delay)
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

        except requests.Timeout:
            if attempt < MAX_RETRIES:
                delay = 2**attempt
                time.sleep(delay)
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

        except requests.ConnectionError:
            if attempt < MAX_RETRIES:
                delay = 2**attempt
                time.sleep(delay)
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

        except requests.RequestException as exc:
            if attempt < MAX_RETRIES:
                delay = 2**attempt
                time.sleep(delay)
                continue
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
