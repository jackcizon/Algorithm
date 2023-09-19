import time
import matplotlib.pyplot as plt
import os

"""
Description:
    Eight Queens Solution Using Recursion
    use 1-d array to represent 2-d matrix

Args:
    n :represent row number
    array[n] or (array[n].val) : represent col number
"""
class Queen:

    def __init__(self) -> None:
        self.max = 8
        self.array = [0] * self.max
        self.count = 0
        self.judgeCount = 0

    def main(self):
        q = Queen()
        q.check()
        print("All solutions have {}\n".format(q.count))
        print("All judegCount: {}\n".format(q.judgeCount)) 

    """
    check if safe

    Args:
        n(int): row number
    
    Returns:
        bool: safe or not
    """
    def judge(self, n):
        self.judgeCount += 1
        for i in range(n):
            if self.array[n] == self.array[i] or abs(n - i) == abs(self.array[n] - self.array[i]):
                return False
        return True

    """
    recursion from n = 0 to n = max
    """
    def check(self, n=0):
        if n == self.max:
            self.print()
            self.count += 1
            return
        for i in range(self.max):
            self.array[n] = i
            if self.judge(n):
                self.check(n + 1)

    def print(self):
        for i in range(self.max):
            for j in range(self.max):
                if self.array[i] == j:
                    print("Q", end=" ")
                else:
                    print("*", end=" ")
            print()
        print("========================\n")
        self.plot_solution()

    """
    Description:
        plot imgs and save in imgs dir
    """
    def plot_solution(self):
        # Create a chessboard visualization
        chessboard = [[0 for _ in range(self.max)] for _ in range(self.max)]
        for i in range(self.max):
            chessboard[i][self.array[i]] = 1

        plt.imshow(chessboard, cmap='binary')
        plt.xticks([])
        plt.yticks()
        if not os.path.isdir("imgs"):
            os.mkdir("imgs")
        plt.savefig("imgs/solution_{}.png".format(self.count+1))  # Save the figure with a unique filename

if __name__ == "__main__":
    start_time = time.time()
    queen = Queen()
    queen.main()
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time: {} seconds".format(execution_time))

