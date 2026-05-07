import hashlib

class IPHashBalancer:
    def __init__(self, servers):
        self.servers = servers

    def next_server(self, client_ip):
        hash_val = int(hashlib.md5(client_ip.encode()).hexdigest(), 16)
        index = hash_val % len(self.servers)
        return self.servers[index]


if __name__ == '__main__':
    iph = IPHashBalancer(["A", "B", "C"])
    ips = ["192.168.1.1", "192.168.1.2", "192.168.1.1"]
    
    ip_1 = []
    for ip in ips:
        ip_1.append(iph.next_server(ip))
    
    ip_2 = []
    for ip in ips:
        ip_2.append(iph.next_server(ip))
    
    assert ip_1 == ip_2
