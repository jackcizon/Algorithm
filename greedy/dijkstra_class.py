class Dijkstra:
    INF = 1 << 21
    WHITE = 0
    GRAY = 1
    BLACK = 2

    def __init__(self, nodes):
        self.nodes = nodes
        self.cost = [[self.INF] * nodes for _ in range(nodes)]
        self.color = [self.WHITE] * nodes
        self.distance = [0] * nodes

    def dijkstra(self, start_node):
        # init all inf, and not visited (white)
        for i in range(self.nodes):
            self.distance[i] = self.INF
            self.color[i] = self.WHITE

        # init distance == 0, mark start point as visited (gray)
        self.distance[start_node] = 0
        self.color[start_node] = self.GRAY

        while True:
            # init min_distance_value as inf and node u as -1
            min_distance_val = self.INF
            u = -1

            # check if the distance distance[j] of the node j
            # from the src node < min_distance_val,
            # and check the node which will be visited is not "cannot be visited" (black)
            for j in range(self.nodes):
                if min_distance_val > self.distance[j] and self.color[j] != self.BLACK:
                    u = j
                    min_distance_val = self.distance[j]

            # it means all nodes are visited (cannot be visited)
            if u == -1:
                break

            self.color[u] = self.BLACK

            # loop all neighbors of node u, check the path value, and update
            for v in range(self.nodes):
                if self.color[v] != self.BLACK and self.cost[u][v] != self.INF:
                    if self.distance[v] > self.distance[u] + self.cost[u][v]:
                        self.distance[v] = self.distance[u] + self.cost[u][v]
                        self.color[v] = self.GRAY

    def get_shortest_path(self, end_node):
        if self.distance[end_node] == self.INF:
            return -1
        else:
            return self.distance[end_node]

# create a new graph with 6 nodes
graph = Dijkstra(6)

# add edges to the graph
graph.cost[0][1] = 4
graph.cost[0][2] = 2
graph.cost[1][2] = 1
graph.cost[1][3] = 5
graph.cost[2][3] = 8
graph.cost[2][4] = 10
graph.cost[3][4] = 2
graph.cost[3][5] = 6
graph.cost[4][5] = 3

# run dijkstra's algorithm on the graph, starting from node 0
graph.dijkstra(0)

# get the shortest path from node 0 to node 5
shortest_path = graph.get_shortest_path(5)

print(f"The shortest path from node 0 to node 5 is: {shortest_path}")  
