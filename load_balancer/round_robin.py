class RoundRobinBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def next_server(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server


    
if __name__ == '__main__':
    rr = RoundRobinBalancer(["A", "B", "C"])
    for _ in range(6):
        print(rr.next_server())
