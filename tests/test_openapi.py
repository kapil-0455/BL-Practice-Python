from pathlib import Path

import yaml


def test_openapi_schema_exists():

    path = Path("openapi.yaml")

    assert path.exists()

    with path.open("r", encoding="utf-8") as file:
        spec = yaml.safe_load(file)

    assert spec["openapi"] == "3.2.0"

    assert "/crawl" in spec["paths"]
    assert "/health" in spec["paths"]
    assert "/results" in spec["paths"]
