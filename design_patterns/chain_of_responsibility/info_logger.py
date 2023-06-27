from chain_of_responsibility.base_logger import BaseLogger


class InfoLogger(BaseLogger):
    def handle(self, log_type: str, log_message: str) -> str:
        if log_type == "INFO":
            return f"{log_type}: {log_message}"
        else:
            return super().handle(log_type, log_message)

