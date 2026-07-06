import sys

class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        self.error_message = error_message

        # Capture the exception traceback if available
        _, _, exc_tb = sys.exc_info()
        if exc_tb:
            self.line_number = exc_tb.tb_lineno
            self.file_name = exc_tb.tb_frame.f_code.co_filename
        else:
            self.line_number = None
            self.file_name = None

    def __str__(self):
        return (
            f"Error occurred in file: {self.file_name}, "
            f"line: {self.line_number}, message: [{self.error_message}]"
        )
