from pyspark.sql import DataFrame
from pyspark.sql.functions import col, count

def check_not_empty(df:DataFrame) -> None:
    """
    Raise ValueError if the dataframe contains no records
    """
    if df.rdd.isEmpty():
        raise ValueError(f"DataFrame is empty")

def check_required_columns(
    df: DataFrame,
    required_columns: list[str]
) -> None:
    """
    Raise ValueError if required columns are missing from the DataFrame.
    """
    df_columns = set(df.columns)
    required_columns_set = set(required_columns)

    missing_columns = required_columns_set - df_columns

    if missing_columns:
        raise ValueError(
            f"DataFrame has missing columns: {missing_columns}"
        )

def check_null_keys(df:DataFrame, key_columns:list[str]) -> None:
    """
    raise ValueError if the key columns contain null values.
    """
    for column in key_columns:
        null_value = df.select(column).filter(col(column).isNull()).limit(1).count()
        if null_value > 0:
            raise ValueError(f"{column} has null value")

def check_duplicate_keys(df:DataFrame, key_columns:list[str]) -> None:
    """
    Raise ValueError if key columns have duplicate keys
    """

    duplicates = df.groupBy(*key_columns).count().filter(col("count") > 1)

    duplicate_count = duplicates.count()

    if duplicate_count > 0:
        sample = duplicates.select(*key_columns).limit(5).collect()
        sample_str = ", ".join(str(row) for row in sample)
        raise ValueError(
            f"Found {duplicate_count} duplicate key combinations."
            f"Example: {sample_str}"
        )