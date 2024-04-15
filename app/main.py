import asyncio
from .encoders import RESP_Simple_String


async def handle_connections(
    reader: asyncio.StreamReader, writer: asyncio.StreamWriter
):
    while True:
        data = await reader.read(1024)
        if not data:
            break

        writer.write(RESP_Simple_String("PONG"))
        await writer.drain()  # flush the writer

    writer.close()
    await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handle_connections, "localhost", 6379)
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
