def partition(arr, low, high):
    pivot = arr[high]
    i = low

    for j in range(low, high):
        
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i] 

    return i


def quick_sort(arr, low, high):

    if low < high:
        pivot = partition(arr, low, high)

        quick_sort(arr, low, pivot - 1)

        quick_sort(arr, pivot + 1, high)


def main():
    arr = [10, 7, 8, 9, 1, 5, 4, 4, 2, 1, 0, -7, 4]

    quick_sort(arr, 0, len(arr) - 1)

    print(arr)

if __name__ == '__main__':
    main() 
