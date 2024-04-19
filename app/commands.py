from . import encoders, database
from datetime import datetime, timedelta


def ping() -> bytes:
    return encoders.simple_string("PONG")


def echo(commands) -> bytes:
    return encoders.bulk_string(commands)


def set_(command) -> bytes:
    entry = database.Entry(command[2])
    if (
        len(command) > 3
    ):  # Check if there are any additional command line arguments (such as PX)
        entry.timeout = datetime.now() + timedelta(milliseconds=int(command[4]))
    database.cache[command[1]] = entry
    return encoders.simple_string("OK")


def get(command) -> bytes:
    time_now = datetime.now()
    entry: database.Entry = database.cache.get(command[1], None)
    if entry is None:
        return encoders.null_bulk_string()

    if entry.timeout and entry.timeout < time_now:
        return encoders.null_bulk_string()

    return encoders.bulk_string(entry.data)


def type_(command) -> bytes:
    entry: database.Entry = database.cache.get(command[1], None)
    if entry is None:
        return encoders.simple_string("none")
    else:
        return encoders.simple_string("string")
