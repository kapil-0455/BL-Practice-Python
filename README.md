# Async Web Intelligence Collector

A Python-based web intelligence collector that compares synchronous HTTP
requests with asynchronous HTTPX execution and uses Crawl4AI for webpage
crawling and content extraction.

---

## 1. Problem Understanding

The objective of this project is to build a small asynchronous web
intelligence system that:

- Accepts product URLs as input.
- Fetches webpages using `requests`.
- Fetches multiple webpages concurrently using `httpx` and `asyncio`.
- Compares sequential and asynchronous execution time.
- Uses Crawl4AI for actual webpage crawling.
- Parses useful product information from crawled content.
- Normalizes extracted data into a common schema.
- Provides an OpenAPI specification as the API contract.
- Handles HTTP errors, connection errors and timeouts.
- Uses pytest for testing and mocking.

The system is designed to demonstrate the difference between
synchronous HTTP execution and asynchronous concurrent execution.

---

## 2. Selected Websites

Three product websites were selected for testing:

1. boAt
2. Noise
3. The Man Company

Example product URLs used in testing:

```text
https://www.boat-lifestyle.com/products/nirvana-ion-bluetooth-wireless-earbuds

https://www.gonoise.com/products/noise-air-buds-truly-wireless-earbuds

https://www.themancompany.com/products/all-about-him

# Architecture
                              USER
                                |
                         3 Product URLs
                                |
              +-----------------+-----------------+
              |                 |                 |
              v                 v                 v
       HTTP BENCHMARK     ACTUAL CRAWLING    API CONTRACT
              |                 |                 |
       +------+-------+         |            openapi.yaml
       |              |         |                 |
       v              v         v                 |
   requests         HTTPX    Crawl4AI             |
   Sequential     + asyncio      |                |
       |            gather       v                |
       |                    Page Content           |
       |                         |                 |
       |                         v                 |
       |                      parser.py            |
       |                         |                 |
       |                      Raw Dict             |
       |                         |                 |
       |                         v                 |
       |                    normalizer.py          |
       |                         |                 |
       |                         v                 |
       |                     Final JSON            |
       |                         |                 |
       |                         v                 |
       |              output/sample_output.json    |
       |                                           |
       +-------------------> benchmark.py <--------+
                                |
                                v
                         Benchmark Report


                              pytest
                                |
                                v
                          Test Suite
                                |
              +-----------------+-----------------+
              |                 |                 |
              v                 v                 v
        HTTP Tests       Processing Tests    Contract Tests
              |                 |                 |
              +-----------------+-----------------+
                                |
                                v
                          Mocking Tests