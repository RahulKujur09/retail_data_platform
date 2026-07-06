from src.common.logger import logger
from src.common.retry import retry
from src.pipelines.silver_pipeline import run_pipeline

DATASETS = [
    "customers",
    "sellers",
    "products",
    "orders",
    "order_items",
    "order_payments",
    "order_reviews",
    "geolocation",
    "product_category_name_translation"
]

@retry("silver pipeline", retries=2, delay_seconds=2.0)
def _run_dataset(dataset: str) -> None:
    logger.info("Running silver for %s", dataset)
    run_pipeline(dataset)


def main():
    for dataset in DATASETS:
        _run_dataset(dataset)

if __name__ == "__main__":
    main()