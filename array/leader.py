'''Array Leaders
find array leaders

The leader of the array is the element on the right side of the array.
The last element of the array must be a leader.

An array usually has at least one leader'''
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

print(find_leaders(10))