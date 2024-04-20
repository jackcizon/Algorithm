'''Major Element

naive approach:
    time complexity: O(n**2)


'''


def naive_method(arr):
    # init counter, max_count
    max_count = 0

    for i in range(len((arr)) - 1):
        counter = 1
        
        for j in range(i + 1, len(arr)):
            if arr[j] == arr[i]:
                counter += 1
        if counter > max_count:
            max_count = counter
            major_ele = arr[i]

    if max_count >= len(arr) // 2:
        return major_ele


def sort_method():
    pass


def boyer_moore_major_voting_algo(arr):
    candidate = -1
    votes = 0

    for i in range(len(arr)):
        if votes == 0:
            candidate = arr[i]
        else:
            if arr[i] == candidate:
                votes += 1
            else:
                votes -= 1
    count = 0

    for i  in range(len(arr)):
        if arr[i] == candidate:
            count += 1
        
    if count > len(arr) // 2:
        return candidate
    else:
        return None

def recursion_method():
    pass



if __name__ == '__main__':
    arr = [1,1,1,1,1,2,2,2,4,5,6,6,6,6,6,6,6,67,6,6,6,6]
    print('init array :>', arr)
    
    print(naive_method(arr))
    