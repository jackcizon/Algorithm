def bucket_sort(arr):
    # Determine the range of input values and the number of buckets
    min_val = min(arr)
    max_val = max(arr)
    bucket_range = (max_val - min_val) / len(arr)
    num_buckets = len(arr)

    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]

    # Place elements into buckets
    for num in arr:
        index = int((num - min_val) / bucket_range)
        if index == num_buckets:  # Handle the case where num is equal to max_val
            index -= 1
        buckets[index].append(num)

    # Sort each bucket (you can use any sorting algorithm here)
    for i in range(num_buckets):
        buckets[i] = sorted(buckets[i])

    # Concatenate the sorted buckets to get the final sorted array
    sorted_array = []
    for i in range(num_buckets):
        sorted_array.extend(buckets[i])

    return sorted_array

# Example usage:
arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)
