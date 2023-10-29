import ipaddress
from enum import Enum, auto
from exceptions import InvalidAddressError, InvalidPortError


# 这是一个网络地址类，进行格式验证。如果后期转发时不需要验证地址有效性，不要用这个类。
class NetAddress:
    def __init__(self, address):
        self.address = address
        self.address_type = self.determine_address_type()
        self.validate_address()

    def determine_address_type(self):
        try:
            ip = ipaddress.ip_address(self.address)
            if ip.version == 4:
                return AddressType.IPv4
            elif ip.version == 6:
                return AddressType.IPv6
            else:
                raise InvalidAddressError(f"无法确定地址类型: {self.address}")
        except ValueError:
            raise InvalidAddressError(f"'{self.address}' 不是一个有效的IP地址")

    def validate_address(self):
        # 现在不需要再验证地址类型，因为它在determine_address_type中确定了
        try:
            ipaddress.ip_address(self.address)
        except ValueError:
            raise InvalidAddressError(f"'{self.address}' 不是一个有效的IP地址")

    def get_address(self):
        return self.address

    def get_address_type(self):
        return self.address_type

    def __str__(self):
        return f"{self.address} 是一个 {self.address_type.name} 地址"


class AddressType(Enum):
    IPv4 = auto()
    IPv6 = auto()


# 这是一个端点类，包含一个地址和一个端口用于处理连接。
class Endpoint:
    def __init__(self, ip_address, port):
        self.ip_address = NetAddress(ip_address)
        if not (0 <= port <= 65535):
            raise InvalidPortError(f"无效的端口号: {port}. 端口号必须在 0 到 65535 之间")  # 验证端口合法性
        self.port = port

    def get_ip_address(self):
        return self.ip_address.get_address()

    def get_port(self):
        return self.port

    def __str__(self):
        return f"{self.ip_address} 端口 {self.port}"
