from queue import Queue

#do not use bool, it is hard to record min path steps
#regard inf as unvisited
inf = 10000


class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def is_valid(maze, x, y):
    return x >= 0 and x < len(maze) and y >= 0 and y < len(maze[0])


def is_blocked(maze, x, y):
    return maze[x][y] == 1


def solve_maze(maze, start, end):

    #init all point not visited
    distance = [[inf for _ in range(len(maze[0]))] for _ in range(len(maze))]

    #use queue to record if there exist point to traverse the maze,
    Q = Queue()
    Q.put(start)

    #init start point as visited
    distance[start.x][start.y] = 0    
    
    #if queue is empty, it means not exist a point to travese, no path
    while not Q.empty():
        #for example, at maze(1, 3), two point will be enqueue to record, 
        #and if 1 path can not get end, then dequeue, and use another point in queue  
        current = Q.get()
        #get the front, and remove it

        #if get end
        if current.x == end.x and current.y == end.y:
            break
        
        #define delta(x, y)
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        '''
            all 4 directions

            (1, 0): right
            (0, 1) : up 
            (-1, 0) : left
            (0, -1): down
        '''
        #explore all directions, and record in visited array
        for i in range(4):
            #record the point location after move
            x = current.x + dx[i]
            y = current.y + dy[i]
            #check if is it feasible to move, not visited, and not blocked
            if is_valid(maze, x, y) and distance[x][y] == inf and not is_blocked(maze, x, y):
                Q.put(point(x, y))
                #we init start[x][y] = 0, 
                #and if find next , then step +1
                distance[x][y] = distance[current.x][current.y] + 1
                #we have set current.x, y,
                #and the start point value is 0

    #the total steps
    return distance[end.x][end.y]

def main():
    # define the maze
    maze = [
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    ]


    # define the start and end points
    start = point(0, 0)
    end = point(9, 8)

    # solve the maze using BFS
    steps = solve_maze(maze, start, end)
    if steps != inf:
        print("Maze solved, total steps : {}".format(steps))
    else:
        print("Maze cannot be solved!")


if __name__ == '__main__':
    main()
