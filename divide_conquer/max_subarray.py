import math
import matplotlib.pyplot as plt

def find_maxcross_subarray(A, low, mid, high):
    left_sum = -math.inf
    max_left = 0
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = -math.inf
    max_right = 0
    sum = 0
    for i in range(mid + 1, high + 1):
        sum += A[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i
    return max_left, max_right, left_sum + right_sum


def find_maxsum_subarray(A, low, high):
    if high == low:
        return low, high, A[low]#one element
    else:
        mid = (low + high) // 2
        left_low, left_high, left_sum = find_maxsum_subarray(A, low, mid)
        right_low, right_high, right_sum = find_maxsum_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum =  find_maxcross_subarray(A, low, mid, high)
        if left_sum > right_sum > cross_sum:
            return left_low, left_high, left_sum
        elif right_sum > left_sum > cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum
        
def gen_data(arr):
    return arr

def get_arr(arr):
    diff_arr = [0] * (len(arr) - 1)
    for i in range(len(diff_arr)):
        diff_arr[i] = arr[i + 1] - arr[i]
    return diff_arr


def main():
    data = gen_data([100, 113, 88, 108, 105, 89, 66, 84, 104, 97, 109, 105, 83, 98, 94, 104])
    diff_arr = get_arr(data)
    print(find_maxsum_subarray(diff_arr, 0, len(diff_arr) - 1))
    # Find the maximum subarray
    max_low, max_high, max_sum = find_maxsum_subarray(diff_arr, 0, len(diff_arr) - 1)
    # Create a bar chart to visualize the price changes
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(diff_arr)), diff_arr, color='b', alpha=0.7, label='Price Change')
    plt.bar(range(max_low, max_high + 1), diff_arr[max_low:max_high + 1], color='r', alpha=0.7, label='Max Stocks')
    plt.xlabel('Date')
    plt.ylabel('Price Change')
    plt.title('Daily Price Change for Company XYZ Stock with Max Subarray Highlighted')
    plt.xticks(range(len(diff_arr)), range(1, len(diff_arr) + 1))
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Display the plot
    plt.tight_layout()
    plt.show()

    # Print the maximum subarray and its sum
    print("Maximum Increment Days:", diff_arr[max_low:max_high + 1])
    print("Maximum Stocks:", max_sum)


if __name__ == '__main__':
    main()

        


