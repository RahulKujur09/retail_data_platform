from src.services.duckdb_loader_service import load_dataset

DATABASE_PATH = "retail.duckdb"

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

def main():
    for dataset in DATASETS:
        load_dataset(
            database_path=DATABASE_PATH,
            dataset_name=dataset,
            parquet_path=f"data/silver/{dataset}"
        )

        print(f"{dataset} loaded into DuckDB")


if __name__ == "__main__":
    main()