from . import encoders


def ping() -> bytes:
    return encoders.simple_string("PONG")


def echo(commands) -> bytes:
    return encoders.bulk_string(commands)
