from enum import Enum, auto


class AddressType(Enum):
    IPv4 = auto()
    IPv6 = auto()
    Invalid = auto()