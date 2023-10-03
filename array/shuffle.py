import random

def array_shuffle(arr):
    n = len(arr)
    for i in range(n):
        j = random.randint(i, n - 1)
        arr[i], arr[j] = arr[j], arr[i]

# Example usage:
arr = [1, 2, 3, 4, 5]
array_shuffle(arr)
print(arr)


'''
In the first iteration (when i is 0), we choose a random index j between 0 and n-1 (inclusive). This means that j has n-1-0+1=n possible choices.

    In the second iteration (when i is 1), we choose a random index j between 1 and n-1, there are n-1-1+1=n-1 choices

    In the third iteration (when i is 2), we choose a random index j between 2 and n-1, with n-1-2+1=n-2 choices
    And so on...
    In the last iteration, there was 1 option

Total result = A(n, n) = n!

Probability = (number of ways this permutation could happen)/(total outcome)

Because each permutation is equally likely to occur, the probability is the same for each permutation, which is 1/n!.
'''