import importlib

from src.common.paths import PROJECT_ROOT
from src.common.reader import read_data
from src.common.writer import write_data
from src.common.silver_config_loader import load_dataset_config

from src.validation.quality import validate_dataframe
from src.common.logger import logger
from src.common.exception import CustomException

from src.monitoring.audit_logger import AuditLogger
from src.monitoring.audit_writer import write_audit_log


def transform_to_silver(
    spark,
    dataset_name: str
):

    try:

        audit = AuditLogger(
            pipeline_name="silver",
            dataset_name=dataset_name
        )

        logger.info(f"Data ingestion to silver layer started for dataset: {dataset_name}")

        config = load_dataset_config(dataset_name)
        
        config.source.path = str(
        PROJECT_ROOT / config.source.path
            )

        config.destination.path = str(
        PROJECT_ROOT / config.destination.path
            )

        transformation = config.transformation

        quality = config.quality

        required_columns = quality.required_columns

        key_columns = quality.key_columns

        df = read_data(
            spark=spark,
            config=config
        )

        records_read = df.count()

        # validate_dataframe(
        #     df=df,
        #     required_columns=required_columns,
        #     key_columns=key_columns
        # )

        # logger.info(f"Validated dataframe for dataset: {dataset_name}")

        logger.info(f"read {records_read} records for dataset: {dataset_name}")

        module = importlib.import_module(
            transformation.module
        )

        transformation_function = getattr(
            module,
            transformation.function
        )

        df = transformation_function(df)

        logger.info(f"Data transformed for dataset: {dataset_name}")

        validate_dataframe(
            df=df,
            required_columns=required_columns,
            key_columns=key_columns
        )

        records_written = df.count()
        logger.info(f"Wrote {records_written} records for dataset: {dataset_name}")

        write_data(
            df=df,
            config=config
        )

        write_audit_log(
            spark=spark,
            audit_record=audit.success(records_read=records_read, records_written=records_written)
        )

        return records_read, records_written
    except Exception as e:
        logger.exception(f"failed to ingest data for dataset: {dataset_name} into silver_layer")
        write_audit_log(spark=spark, audit_record=audit.failure(str(e)))
        raise CustomException(str(e))