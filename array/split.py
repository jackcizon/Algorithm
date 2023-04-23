def split(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        while arr[i] % 2 != 0:
            i += 1
        
        while arr[j] % 2 == 0:
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]


def main():
    arr = [5, 7, 2, 3, 1, 4, 7, 8, 10, 0, 5, 4]
    split(arr)
    print(arr)


if __name__ == '__main__':
    main()