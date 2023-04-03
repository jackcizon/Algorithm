'''
    W represents the sunken surface, 
    Which can receive rainWater to form lakes, 
    and * represents the ground.
'''

'''
    a lake maybe like this :

        ***********W**
        **WWWW******W*
        ****WWWWWWWW**
        **WWWW******W*

    in all 8 directions, all W.

    first set a point x,y = 0, 0
    then the 8 directions coordinates should be

            -1, -1 |-1, 0 | -1, 1
                   |      |
            0, -1  | 0, 0 |  0, 1 
                   |      |
            1, -1  | 1, 0 |  1, 1

    and We use DFS(), to check if there is a lake,

    to avoid repeat, after find W, set_to *.
'''


def DFS(field, x, y):
    
    #set point as visited
    field[x][y] = '*'

    #move all 8 directions
    for dx in range(-1, 2, 1):
        for dy in range(-1, 2, 1):
            #move result
            nx = x + dx
            ny = y + dy

            #check
            if 0 <= nx and 0 <= ny and nx < len(field) and ny < len(field[0]) and field[nx][ny] == 'W':
                DFS(field, nx, ny)



def lake_counting(field):
    count = 0
    for x in range(len(field)):
        for y in range(len(field[0])):
            if(field[x][y] == 'W'):
                DFS(field, x, y)
                #DFS() loop end, then lake + 1
                count += 1
    return count


def main():
    field = [
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', '*', 'W', 'W', '*', '*', '*', '*', '*', '*', '*', '*'],
        ['*', 'W', '*', '*', 'W', '*', '*', 'W', '*', 'W', '*', '*'],
        ['*', '*', 'W', '*', '*', '*', '*', '*', 'W', '*', '*', '*']
            ]
    
    print(lake_counting(field))
    #lakes_count = 2

if __name__ == '__main__':
    main()
    
