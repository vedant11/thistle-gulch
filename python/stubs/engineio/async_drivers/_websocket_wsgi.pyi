from _typeshed import Incomplete

class SimpleWebSocketWSGI:
    app: Incomplete
    server_args: Incomplete
    def __init__(self, handler, server, **kwargs) -> None: ...
    ws: Incomplete
    def __call__(self, environ, start_response): ...
    def close(self) -> None: ...
    def send(self, message): ...
    def wait(self): ...
