class Server:
    def __init__(self, name):
        self.name = name
        self.connections = 0


class LeastConnectionsBalancer:
    def __init__(self, servers):
        self.servers = [Server(name) for name in servers]

    def next_server(self):
        least = self.servers[0]

        for s in self.servers[1:]:
            if s.connections < least.connections:
                least = s

        least.connections += 1
        return least

    def release(self, server):
        if server.connections > 0:
            server.connections -= 1


if __name__ == '__main__':
    lb = LeastConnectionsBalancer(["A", "B", "C"])

    for i in range(10):
        s = lb.next_server()
        print(s.name, s.connections)