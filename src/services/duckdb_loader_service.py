import duckdb

def load_dataset(
        database_path : str,
        dataset_name : str,
        parquet_path : str
        ) -> None:
    
    connection = duckdb.connect(database_path)

    connection.execute(
        f"""
            CREATE OR REPLACE TABLE {dataset_name} AS
            SELECT
                *
            FROM read_parquet('{parquet_path}/*.parquet')
        """
    )

    connection.close()