import asyncio
from . import commands as redis_commands
from typing import List
from . import encoders as redis_encoders


def parse_command(command: bytes) -> List[str]:
    command_string = command.decode()
    # limit string to only commands by trimming the beginning
    # of the command string which contains the number of
    # commands being sent to the redis server
    first_element = command_string.find(
        "$"
    )  # find first instance of '$' which is in front of each command
    commands = command_string[first_element + 1 :].split(
        "$"
    )  # `first_element + 1` to avoid an empty element in the beginning

    decoded_commands = []
    for comm in commands:
        decoded_commands.append(redis_encoders.bulk_string(comm, decode=True))

    print(decoded_commands)
    return decoded_commands


def handle_input(input_data) -> bytes:
    commands = []  # array of all commands given by the client
    commands = parse_command(input_data)

    # The first command is the function we need to call
    function = commands[0].lower()

    if function == "echo":
        return redis_commands.echo(commands[1])
    elif function == "ping":
        return redis_commands.ping()
    elif function == "set":
        return redis_commands.set_(commands)
    elif function == "get":
        return redis_commands.get(commands)


async def handle_connections(
    reader: asyncio.StreamReader, writer: asyncio.StreamWriter
):
    while True:
        data = await reader.read(1024)
        if not data:
            break

        writer.write(handle_input(data))
        await writer.drain()  # flush the writer

    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_connections, "localhost", 6379)
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
