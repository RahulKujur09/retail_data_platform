from datetime import datetime
import uuid

class AuditLogger:
    def __init__(self, pipeline_name:str, dataset_name:str):
        self.pipeline_name = pipeline_name
        self.dataset_name = dataset_name

        self.run_id = str(uuid.uuid4())
        self.start_time = datetime.now()

    def success(self, records_read: int | None, records_written: int | None) -> dict:
        end_time = datetime.now()

        return {
            "run_id" : self.run_id,
            "pipeline_name" : self.pipeline_name,
            "dataset_name" : self.dataset_name,
            "start_time" : self.start_time,
            "end_time" : end_time,
            "duration_seconds" : (
                end_time - self.start_time
            ).total_seconds(),
            "status" : "SUCCESS",
            "records_read" : records_read,
            "records_written": records_written,
            "error_message" : None
        }
    
    def failure(self, error_message : str) -> dict:
        end_time = datetime.now()

        return {
            "run_id" : self.run_id,
            "pipeline_name" : self.pipeline_name,
            "dataset_name" : self.dataset_name,
            "start_time" : self.start_time,
            "end_time" : end_time,
            "duration_seconds" : (
                end_time - self.start_time
            ).total_seconds(),
            "status" : "FAILED",
            "records_read" : None,
            "records_written" : None,
            "error_message" : error_message
        }

