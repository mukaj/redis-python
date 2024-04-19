from . import encoders, database


def ping() -> bytes:
    return encoders.simple_string("PONG")


def echo(commands) -> bytes:
    return encoders.bulk_string(commands)


def set_(command) -> bytes:
    database.cache[command[1]] = command[2]
    return encoders.simple_string("OK")


def get(command) -> bytes:
    return encoders.bulk_string(database.cache[command[1]])
