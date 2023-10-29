import ipaddress

from Communications.AddressType import AddressType


class NetAddress:
    def __init__(self, address):
        self.address = address
        self.address_type = self.get_address_type()

    def get_address_type(self):
        try:
            ip = ipaddress.ip_address(self.address)
            if ip.version == 4:
                return AddressType.IPv4
            elif ip.version == 6:
                return AddressType.IPv6
            else:
                return AddressType.Invalid
        except ValueError:
            return AddressType.Invalid

    def get_address(self):
        return self.address

    def __str__(self):
        return f"{self.address} is a {self.address_type.name} address"