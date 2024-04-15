import socket
from .encoders import RESP_Simple_String


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    client_socket, client_address = server_socket.accept()  # wait for client

    # Send PONG message to client
    client_socket.sendall(
        RESP_Simple_String("PONG")
    )  # socket.sendall is used to ensure that all the bytes are sent to the client


if __name__ == "__main__":
    main()
