import time

import requests

DEFAULT_TIMEOUT = 10
MAX_RETRIES = 3


def fetch_page(url: str) -> dict:

    for attempt in range(MAX_RETRIES + 1):
        try:
            start_time = time.perf_counter()
            response = requests.get(url, DEFAULT_TIMEOUT)

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

        except requests.Timeout:
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

        except requests.ConnectionError:
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

        except requests.RequestException as exc:
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
