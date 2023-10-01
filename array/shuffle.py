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
在第一次迭代中（当 i 为 0 时），我们选择一个介于 0 和 n-1（含）之间的随机索引 j。这意味着 j 有 n 个可能的选择。

    在第二次迭代中（当 i 为 1 时），我们在 1 和 n-1 之间选择一个随机索引 j吗，有n种选择

    在第三次迭代中（当 i 为 2 时），我们在 2 和 n-1 之间选择一个随机索引 j，有n-1种选择
    以此类推...
    在最后一次迭代中,有1种选择

总结果 = A(n, n) = n!

概率 =（这种排列可能发生的方式数量）/（总结果）

因为每个排列发生的可性相同，对于每个排列，概率是相同的，该概率为 1/n!。
'''