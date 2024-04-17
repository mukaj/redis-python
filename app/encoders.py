def simple_string(data: str, decode=False) -> bytes | str:
    """
    Encode and Decode a string according to Redis' "RESP Simple Strings"
    https://redis.io/docs/latest/develop/reference/protocol-spec/#simple-strings
    """

    if not decode:
        return f"+{data}\r\n".encode(encoding="utf-8")
    else:
        # The simple string content is the same as the data string,
        # only without the plus symbol in the beginning and without the
        # CRLF characters in the end.
        return data[1:-2]


def bulk_string(data: str, decode=False) -> bytes | str:
    """
    Encode and Decode a string according to Redis' "RESP Bulk Strings"
    https://redis.io/docs/latest/develop/reference/protocol-spec/#bulk-strings
    """

    if not decode:
        return f"${len(data)}\r\n{data}\r\n".encode(encoding="utf-8")
    else:
        # The start is past the first instance of CRLF
        start = data.find("\r\n") + 2
        # The end is before the last instance of CRLF
        end = data.rfind("\r\n")
        return data[start:end]
