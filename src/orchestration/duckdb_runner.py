from src.common.logger import logger
from src.common.retry import retry
from src.services.duckdb_loader_service import load_dataset
from src.common.paths import PROJECT_ROOT

DATABASE_PATH = str(PROJECT_ROOT / "retail.duckdb")

DATASETS = [
    "customers",
    "geolocation",
    "order_items",
    "order_payments",
    "order_reviews",
    "orders",
    "products",
    "sellers",
]


@retry("duckdb load", retries=2, delay_seconds=2.0)
def _load_dataset(dataset: str) -> None:
    logger.info("Loading %s into DuckDB", dataset)
    load_dataset(
        database_path=DATABASE_PATH,
        dataset_name=dataset,
        parquet_path=str(PROJECT_ROOT / "data" / "silver" / dataset)
    )


def main():
    for dataset in DATASETS:
        _load_dataset(dataset)
        logger.info("%s loaded into DuckDB", dataset)


if __name__ == "__main__":
    main()