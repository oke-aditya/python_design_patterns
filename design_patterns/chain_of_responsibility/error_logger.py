from chain_of_responsibility.base_logger import BaseLogger


class ErrorLogger(BaseLogger):
    def handle(self, log_type: str, log_message: str) -> str:
        if log_type == "ERROR":
            return f"{log_type}: {log_message}"
        else:
            return super().handle(log_type, log_message)
