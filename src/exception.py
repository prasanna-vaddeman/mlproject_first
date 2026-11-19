import sys

class CustomException(Exception):
    """Base class for custom exception."""

    def __init__(self, error_message: str, error_details=sys):
        super().__init__(error_message)

        self.error_message = error_message
        self.error_details = error_details

        _, _, tb_exc = error_details.exc_info()

        while tb_exc and tb_exc.tb_next:
            tb_exc = tb_exc.tb_next

        self.line_number = tb_exc.tb_lineno if tb_exc else None
        self.file_name = tb_exc.tb_frame.f_code.co_filename if tb_exc else None

    def __str__(self) -> str:
        return (
            f"Error occurred in script: [{self.file_name}]",
            f"at line number: [{self.line_number}]",
            f"Error message: [{self.error_message}]"
        )