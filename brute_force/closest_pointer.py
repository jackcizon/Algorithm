import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Distance(Point):
    def distance(p1, p2):
        return math.sqrt(
            (p1.x - p2.x) *(p1.x - p2.x) 
            + (p1.y - p2.y) * (p1.y - p2.y)
        )


class BruteForce(Distance):
    def min_len(P, size):
        min_val = float('inf')

        for i in range(size):

            for j in range(i + 1, size):
                
                if Distance.distance(P[i], P[j]) < min_val:
                    min_val = Distance.distance(P[i], P[j])
        
        return min_val


P = [
        Point(2, 3), Point(12, 30),
        Point(40, 50), Point(5, 1),
        Point(12, 10), Point(3, 4)
    ]


print("smallest distance:", BruteForce.min_len(P, len(P)))
