class WeightedRoundRobinBalancer:
    def __init__(self, weighted_servers):
        # weighted_servers = [("A",3), ("B",1), ("C",1)]
        self.pool = []
        for server, weight in weighted_servers:
            self.pool.extend([server] * weight)
        self.index = 0

    def next_server(self):
        server = self.pool[self.index]
        self.index = (self.index + 1) % len(self.pool)
        return server


if __name__ == '__main__':
    wrr = WeightedRoundRobinBalancer([("A", 3), ("B", 1), ("C", 1)])
    for _ in range(10):
        print(wrr.next_server())
