import sys

from src.common.spark import create_spark_session
from src.services.bronze_ingestion_service import ingest_to_bronze


def run_pipeline(dataset_name: str):

    spark = create_spark_session()

    try:
        ingest_to_bronze(
            spark=spark,
            dataset_name=dataset_name
        )
    finally:
        spark.stop()


def main():

    if len(sys.argv) != 2:
        raise Exception(
            "Usage : python bronze_pipeline.py customers"
        )

    run_pipeline(sys.argv[1])


if __name__ == "__main__":
    main()