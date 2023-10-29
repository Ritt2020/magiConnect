import asyncio
import socket


async def send_tcp(server_ip, server_port, data):
    try:
        reader, writer = await asyncio.open_connection(server_ip, server_port)
        print(f"连接到 {server_ip}:{server_port} 成功")
        writer.write(data.encode())
        await writer.drain()
        writer.close()
        await writer.wait_closed()
        print("TCP数据发送成功")
    except Exception as e:
        print(f"无法连接到 {server_ip}:{server_port}: {e}")


async def send_udp(server_ip, server_port, data):
    try:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.sendto(data.encode(), (server_ip, server_port))
        udp_socket.close()
        print(f"UDP数据发送成功到 {server_ip}:{server_port}")
    except Exception as e:
        print(f"无法发送UDP数据到 {server_ip}:{server_port}: {e}")


if __name__ == '__main__':
    asyncio.run(send_tcp("127.0.0.1", 8081, "Hello, TCP Server!"))
    asyncio.run(send_udp("127.0.0.1", 8081, "Hello, UDP Server!"))
