import subprocess
from src.pipelines import bronze_pipeline
from src.pipelines import silver_pipeline
from src.orchestration.silver_runner import main as load_silver_to_duckdb


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


def main():

    for dataset in DATASETS:

        print(f"Running bronze for {dataset}")

        bronze_pipeline.run_pipeline(dataset)

        print(f"Running silver for {dataset}")

        silver_pipeline.run_pipeline(dataset)
    
    load_silver_to_duckdb()

    subprocess.run(["dbt", "run"], cwd="dbt", check=True)
    
    subprocess.run(["dbt", "snapshot"], cwd="dbt", check=True)
    
    # subprocess.run(["dbt", "run"], cwd="dbt", check=True)


if __name__ == "__main__":
    main()