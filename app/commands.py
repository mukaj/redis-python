from . import encoders


def ping() -> bytes:
    return encoders.simple_string("PONG")


def echo(commands):
    return encoders.bulk_string(commands)
