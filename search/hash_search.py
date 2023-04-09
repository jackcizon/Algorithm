def _hash(value, size):
    return value % size

def insert(arr, value):
    key = _hash(value, len(arr))
    arr[key] = value

def hash_search(arr, value, size):
    key = _hash(value, size)
    return True if arr[key] == value else False


arr = [0 for _ in range(3)]

insert(arr, 3)#0
insert(arr, 5)#2
insert(arr, 7)#1


print(hash_search(arr, 2, len(arr)))
print(hash_search(arr, 5, len(arr)))
