import sys

class CustomException(Exception):
    """Base class for custom exception."""

    def __init__(self, error_message: str, error_details=sys):
        super().__init__(error_message)

        self.error_message = error_message
        self.error_details = error_details

        _, _, exc_tb = error_details.exc_info()

        while exc_tb and exc_tb.tb_next:
            exc_tb = exc_tb.tb_next

        self.line_number = exc_tb.tb_lineno if exc_tb else None
        self.file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else None

    def __str__(self) -> str:
        return (
            f"Error occurred in script: [{self.file_name}]",
            f"at line number: [{self.line_number}]",
            f"Error message: [{self.error_message}]"
        )