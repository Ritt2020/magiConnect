import asyncio
import socket
import socket, threading


class SimpleServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        # 创建一个TCP/IP套接字
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)  # 最大连接数为5

        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.bind((self.host, self.port))

        print(f"正在监听TCP/UDP端口 {self.host}:{self.port}")

        tcp_thread = threading.Thread(target=self._handle_tcp_connections, args=(server_socket,))
        udp_thread = threading.Thread(target=self._handle_udp_messages, args=(udp_socket,))

        tcp_thread.start()
        udp_thread.start()

        tcp_thread.join()
        udp_thread.join()

    def _handle_tcp_connections(self, server_socket):
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"收到连接 {client_address}")
            client_thread = threading.Thread(target=self._handle_tcp_client, args=(client_socket,))
            client_thread.start()

    def _handle_tcp_client(self, client_socket):
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"收到TCP消息: {data.decode()}")
        client_socket.close()

    def _handle_udp_messages(self, udp_socket):
        while True:
            data, client_address = udp_socket.recvfrom(1024)
            print(f"收到UDP消息 {client_address}: {data.decode()}")


if __name__ == "__main__":
    server = SimpleServer("127.0.0.1", 8081)
    server.start()
