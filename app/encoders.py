def RESP_Simple_String(string: str) -> bytes:
    """
    Encode a string according to Redis' "RESP Simple Strings"
    https://redis.io/docs/latest/develop/reference/protocol-spec/#simple-strings
    """
    return bytes(f"+{string}\r\n", "utf-8")
