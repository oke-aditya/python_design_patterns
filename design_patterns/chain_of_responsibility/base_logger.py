from chain_of_responsibility.base_handler import BaseHandler


class BaseLogger(BaseHandler):
    _next_handler: BaseHandler = None

    def set_next(self, handler: BaseHandler) -> BaseHandler:
        self._next_handler = handler
        return handler

    def handle(self, log_type: str, log_message: str) -> str:
        if self._next_handler:
            return self._next_handler.handle(log_type, log_message)
        return None
