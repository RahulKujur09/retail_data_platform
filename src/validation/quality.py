from pyspark.sql import DataFrame

from src.validation.rules import (
    check_not_empty,
    check_required_columns,
    check_null_keys,
    check_duplicate_keys
)

def validate_dataframe (
        df:DataFrame,
        required_columns : list[str],
        key_columns : list[str] | None = None
) -> None:
    check_not_empty(df)

    check_required_columns(
        df,
        required_columns
        )
    if key_columns:
        check_null_keys(
            df,
            key_columns
            )
        
        check_duplicate_keys(
            df,
            key_columns
        )