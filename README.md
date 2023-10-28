# magiConnect
A simple distributed networking program.
## Develop
1. Implementing TCP and UDP communications between server and client using socket. Server prints everything receiving, client send random string.
2. Create a module generating CA.
3. Encrypt TCP/UDP data  with CA(like TLS).
4. TODO

#ifndef NODE_H
#define NODE_H

class node
{
private:
    /* data */
public:
    node(/* args */);
    ~node();
};

node::node(/* args */)
{
}

node::~node()
{
}
#endif完成这个类 node包含一个枚举类型，类型为叶子节点LEAF或者内核节点KERNEL 。包含了两个布尔值，分别代表ipv4和ipv6地址是否已经可用。还包含两个ipv4和ipv6是否可被外部访问的布尔值。然后保存ipv4地址和ipv6地址，和对应的两个监听端口。还需要用合适的结构保存一个包含多个网段信息的列表或者集合，每个网段信息都有一个说明类型是v4或者v6的布尔值，一个ip地址和一个子网前缀长度。