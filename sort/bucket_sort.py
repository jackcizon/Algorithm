def bucket_sort(arr):
    bucket = []
    #init bucket
    for i in range(0, 11, 1):
        bucket.append(0)
    #join bucket and count
    for i in range(0, len(arr), 1):
        val = arr[i]
        bucket[val] += 1
    #sort array
    j = 0
    for i in range(0, len(bucket), 1):
        val = bucket[i]
        while val != 0:
            arr[j] = i
            j += 1
            val -= 1
    pass



def main():
    arr = [3, 1, 6, 8, 5, 4, 4, 2, 0]
    bucket_sort(arr)
    print(arr)
    pass


if __name__ == '__main__':
    main()
    pass