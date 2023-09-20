class StepSolver:
    def __init__(self, high):
        self.high = high
        self.path = [0] * high
        self.num = 0

    def solve(self):
        self._try_steps(self.high, 0)

    def _try_steps(self, high, step_count):
        if high == 0:
            self.num += 1
            solution = "Solution {}: ".format(self.num)
            for i in range(step_count):
                solution += str(self.path[i]) + " "
            print(solution)
            print("================")
        for i in range(1, 4):
            new_high = high - i
            if new_high >= 0:
                self.path[step_count] = i
                self._try_steps(new_high, step_count + 1)

high = 5
solver = StepSolver(high)
solver.solve()
