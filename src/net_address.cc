#include "net_address.h"
#include <arpa/inet.h>

net_address::net_address(const std::string& ip_address) {
    if (inet_pton(AF_INET, ip_address.c_str(), &v4_address) == 1) {
        is_ipv4 = true;
        is_ipv6 = false;
    } else if (inet_pton(AF_INET6, ip_address.c_str(), &v6_address) == 1) {
        is_ipv4 = false;
        is_ipv6 = true;
    } else {
        is_ipv4 = false;
        is_ipv6 = false;
    }
    ip_address_str = ip_address;
}

bool net_address::is_ipv4_address() const {
    return is_ipv4;
}

bool net_address::is_ipv6_address() const {
    return is_ipv6;
}

std::string net_address::get_ip_address_str() const {
    return ip_address_str;
}
