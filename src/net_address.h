#ifndef NET_ADDRESS_H
#define NET_ADDRESS_H

#include <string>

class net_address {
public:
    net_address(const std::string& ip_address);

    bool is_ipv4_address() const;
    bool is_ipv6_address() const;
    std::string get_ip_address_str() const;

private:
    bool is_ipv4;
    bool is_ipv6;
    std::string ip_address_str;
    struct in_addr v4_address;
    struct in6_addr v6_address;
};

#endif // NET_ADDRESS_H
