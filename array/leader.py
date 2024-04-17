'''Array Leaders
find array leaders

The leader of the array is the element on the right side of the array.
The last element of the array must be a leader.

An array usually has at least one leader

native approach:
    Time Complexity: O(n**2)
    space Complexity: O(n)

max_suffix approach:
    Time Complexity: O(n)
    space Complexity: O(n)
'''
import random

def find_leaders(size: int) -> list:
    #gen random array
    arr: list = [random.randint(1, 100) for _ in range(size)]

    print('init array :> ', arr)

    # find leaders
    leaders = []

    for i in range(size):
        for j in range(i + 1, size):
            if arr[i] <= arr[j]:
                break
            if j == size - 1:
                leaders.append(arr[i])
    leaders.append(arr[-1])

    return leaders


def find_max_suffix(size: int) -> list:
    # init leaders 
    leaders: list = []
    
    arr = [random.randint(1, 100) for _ in range(size)]
    print('init array :> ', arr)

    leaders.append(arr[-1])
    
    # define max item
    max_item = arr[-1]
    for i in range(size - 1, -1, -1):
        if arr[i] > max_item:
            leaders.append(arr[i])
            max_item = arr[i]

    return leaders


if __name__ == '__main__':
    # print('native approach :> ')
    # print(find_leaders(10))
    
    print('finding suffix max approach: :>')
    print('leaders :> ', find_max_suffix(10))