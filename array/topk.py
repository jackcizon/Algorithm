'''Bubble Sort Implementation

Time Complexity: O(m*n)
'''

def bubble_sort_top_k(arr, k):
    n = len(arr)
    for i in range(k):  # Perform k iterations
        for j in range(n - 1, i, -1):
            if arr[j] > arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    
    return arr[:k]  # Return the top k elements

# Example usage:
arr = [3, 1, 8, 4, 7, 6, 2, 5]
k = 3
top_k_elements = bubble_sort_top_k(arr, k)
print("Top", k, "elements:", top_k_elements)
