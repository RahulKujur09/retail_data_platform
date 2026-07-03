import sys

from  src.common.spark import create_spark_session
from src.monitoring.audit_logger import AuditLogger
from src.services.silver_transformation_service import transform_to_silver

from src.monitoring.audit_writer import write_audit_log


def run_pipeline(dataset_name: str):

    spark = create_spark_session()

    audit = AuditLogger(
        pipeline_name="silver_pipeline",
        dataset_name=dataset_name
    )

    try:

        records_read, records_written = transform_to_silver(
            spark=spark,
            dataset_name=dataset_name
        )

        audit_record = audit.success(
            records_read=records_read,
            records_written=records_written
        )

        write_audit_log(
            spark=spark,
            audit_record=audit_record
        )

    except Exception as e:

        audit_record = audit.failure(
            error_message=str(e)
        )

        write_audit_log(
            spark=spark,
            audit_record=audit_record
        )

        raise

    finally:
        spark.stop()


def main():

    if len(sys.argv) != 2:
        raise Exception(
            "Usage : python silver_pipeline.py customers"
        )

    run_pipeline(sys.argv[1])


# if __name__ == "__main__":
#     main()