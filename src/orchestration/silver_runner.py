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

def main():
    for dataset in DATASETS:
        print(f"Running silver for {dataset}")
        run_pipeline(dataset)

if __name__ == "__main__":
    main()