max = 100
inf = 1 << 21
white = 0
gray = 1
black = 2

def dijkstra(nodes, distance, color, cost):
    #init all inf, and not visted(white)
    for i in range(nodes):
        distance[i] = inf
        color[i] = white
    #init distance == 0, mark start point as visted(gray)
    distance[0] = 0
    color[0] = gray

    while(True):
        #init min_distance_value as inf nad node u as -1
        min_distance_val = inf
        u = -1
        #check if the distance distance[j] of the node j
        #from the src node < min_distance_val,
        #and check the node which will visited is not 'cannot visited'(black)
        for j in range(nodes):
            if min_distance_val > distance[j] and color[j] != black:
                u = j
                min_distance_val = distance[j]
        #it means all nodes are visited(cannot visited)
        if u == -1:
            break
        color[u] = black

        #loop all neighbors of node u, check the path value, and update
        for v in range(nodes):
            if color[v] != black and cost[u][v] != inf:
                if distance[v] > distance[u] + cost[u][v]:
                    distance[v] = distance[u] + cost[u][v]
                    color[v] = gray

    for k in range(nodes):
        if distance[k] == inf:
            print("{} -1\n".format(k))
        else:
            print("{} {}\n".format(k, distance[k]))


def main():
    nodes = 6  # number of nodes
    inf = 1 << 21
    cost = [[inf] * nodes for i in range(nodes)]  # adjacency matrix
    color = [0] * nodes  # node colors (0=white, 1=gray, 2=black)
    distance = [0] * nodes  # shortest path distances

    # add edges to the graph
    cost[0][1] = 4
    cost[0][2] = 2
    cost[1][2] = 1
    cost[1][3] = 5
    cost[2][3] = 8
    cost[2][4] = 10
    cost[3][4] = 2
    cost[3][5] = 6
    cost[4][5] = 3

    # find the shortest path between nodes 0 and 5
    start_node = 0
    end_node = 5
    dijkstra(nodes, distance, color, cost)
    shortest_dist = distance[end_node]

    # print the result
    if shortest_dist == inf:
        print(f"No path from node {start_node} to node {end_node} exists.")
    else:
        print(f"The shortest distance from node {start_node} to node {end_node} is {shortest_dist}.")



if __name__ == '__main__':
    main()
