from queue import Queue

class Pair():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def is_valid(maze, row, column):
    return 0 <= row < len(maze) and\
            0 <= column < len(maze[0])


def is_blocked(maze, row, column):
    return maze[row][column] == 1


def solve_maze(maze, start, end):
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]

    visited[start.x][start.y] = True

    #use queue to record if there exist point to traverse the maze,
    Q = Queue()
    Q.put(start)
    
    #if queue is empty, it means not exist a point to travese, no path
    while not Q.empty():
        #for example, at maze(1, 3), two point will be enqueue to record, 
        #and if 1 path can not get end, then dequeue, and use another point in queue  
        current = Q.get()
        row = current.x
        column = current.y

        #if get end
        if row == end.x and column == end.y:
            return True
        
        #define delta(x, y)
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        '''
            all 4 directions

            (-1, 0): left
            (0, 1) : right 
            (1, 0) : up
            (0, -1): down
        '''
        #explore all directions, and record in visited array
        for i in range(3):
            r = row + dx[i]
            c = column + dy[i]
            if is_valid(maze, r, c) and not visited[r][c] and not is_blocked(maze, r, c):
                 visited[r][c] = True
                 Q.put(Pair(r, c))

    return False

def main():
    # define the maze
    maze = [
        [0, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 0]
    ]

    # define the start and end points
    start = Pair(0, 0)
    end = Pair(8, 7)

    # solve the maze using BFS
    if solve_maze(maze, start, end):
        print("Maze solved!")
    else:
        print("Maze cannot be solved!")


if __name__ == '__main__':
    main()
