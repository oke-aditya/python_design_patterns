from chain_of_responsibility.info_logger import InfoLogger
from chain_of_responsibility.error_logger import ErrorLogger


def log(log_type: str, log_msg: str):
    info_logger = InfoLogger()
    error_logger = ErrorLogger()

    error_logger.set_next(info_logger)

    res = error_logger.handle(log_type, log_msg)
    print(res)


if __name__ == "__main__":
    log("INFO", "This is some info")
