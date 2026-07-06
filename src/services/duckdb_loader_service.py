import duckdb
from src.common.logger import logger
from src.common.exception import CustomException

def load_dataset(
        database_path : str,
        dataset_name : str,
        parquet_path : str
        ) -> None:
    try:
        logger.info(f"connecting to data_base.")
        connection = duckdb.connect(database_path)

        connection.execute(
            f"""
                CREATE OR REPLACE TABLE {dataset_name} AS
                SELECT
                    *
                FROM read_parquet('{parquet_path}/*.parquet')
            """
        )
        logger.info(f"{dataset_name} written into the data_base")

        connection.close()
    except Exception as e:
        logger.info(f"Failed to write the data into data_base for dataset: {dataset_name}")
        raise CustomException(str(e))
