import importlib
from pyspark.sql.utils import AnalysisException

from src.common.paths import PROJECT_ROOT
from src.common.bronze_config_loader import load_dataset_config
from src.common.reader import read_data
from src.common.writer import write_data

from src.services.enrichment import add_metadata
from src.validation.quality import validate_dataframe

from src.common.logger import logger
from src.common.exception import CustomException

from src.monitoring.audit_logger import AuditLogger

from src.monitoring.audit_writer import write_audit_log

from src.common.incremental_loader import get_incremental_records

def ingest_to_bronze(
    spark,
    dataset_name: str
):
    logger.info(f"Starting bronze ingestion for dataset: {dataset_name}")

    try:
        audit = AuditLogger(pipeline_name="bronze", dataset_name=dataset_name)
        config = load_dataset_config(dataset_name)

        config.source.path = str(
            PROJECT_ROOT / config.source.path
        )

        config.destination.path = str(
            PROJECT_ROOT / config.destination.path
        )

        module = importlib.import_module(
            config.schema.module
        )

        schema = getattr(
            module,
            config.schema.variable
        )

        source_df = read_data(
            spark=spark,
            config=config,
            schema=schema
        )

        records_read = source_df.count()

        logger.info(f"Read dataset: {dataset_name}")

        try:
            target_df = spark.read.parquet(config.destination.path)
            logger.info(f"Bronze dataset found for dataset {dataset_name}")
        except AnalysisException:
            target_df = None
            logger.info(f"Bronze dataset not found for dataset {dataset_name}")

        df = get_incremental_records(
            source_df=source_df,
            target_df=target_df,
            key_columns=config.quality.key_columns
        )


        records_written = df.count()

        if records_written == 0:
            logger.info("No new records found")
            write_audit_log(
                spark=spark,
                audit_record=audit.success(records_read=records_read, records_written=records_written)
            )

            return
        
        validate_dataframe(
            df=df,
            required_columns=config.quality.required_columns,
            key_columns=config.quality.key_columns
        )

        logger.info(
            f"Validated dataframe: {dataset_name}"
        )

        df = add_metadata(
            df=df,
            dataset_name=dataset_name
        )

        logger.info(
            f"Added metadata: {dataset_name}"
        )

        write_data(
            df=df,
            config=config
        )

        write_audit_log(spark=spark, audit_record=audit.success(records_read=records_read, records_written=records_written))

        logger.info(
            f"Wrote bronze parquet: {dataset_name}"
        )

        logger.info(
            f"Bronze ingestion completed for {dataset_name}"
        )

    except Exception as e:
        logger.exception(
            f"Bronze ingestion failed for {dataset_name}"
        )
        write_audit_log(spark=spark, audit_record=audit.failure(str(e)))
        raise CustomException(str(e))