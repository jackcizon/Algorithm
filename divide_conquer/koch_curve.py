'''
    fractional coordinates:
        * *    *
        a x    b
    
        bx = n*ax
        x = (n*ax + 1*bx)/(n+1)
'''

'''
    rotation matrix:

        | cos(theta) -sin(theta) |   | x |     | x' |
        | sin(theta)  cos(theta) | * | y |  =  | y' |

        cos(thete)*x - sin(theta)*y = x'
        sin(theta)*x + cos(theta)*y = y'

       x = t.x - s.x
       y = t.y - s.y

        start from s, Rotate t 'x' degrees counterclockwise to get u

        the coordinate of u is related to s,
        so must add s.x, s.y to relate to original coordinate.

        
    u.x = (t.x - s.x)*cos(x) - (t.y - s.y)*sin(x) + s.x
    u.x = (t.x - s.x)*sin(x) - (t.y - s.y)*cos(x) + s.y
'''

'''
      u
     /\ 
____/  \____
p1  s   t   p2    
'''

from math import sin, cos

class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def koch(order, p1, p2):
    if order == 0:
        return
    
    pi = 3.1415926
    theta = pi * 60 / 180

    s = point(0, 0)
    t = point(0, 0)
    u = point(0, 0)

    s.x = (2.0*p1.x + 1.0*p2.x) / 3.0
    s.y = (2.0*p1.y + 1.0*p2.y) / 3.0

    t.x = (2.0*p2.x + 1.0*p1.x) / 3.0
    t.y = (2.0*p2.y + 1.0*p1.y) / 3.0

    u.x = (t.x - s.x)*cos(theta) - (t.y - s.y)*sin(theta) + s.x
    u.y = (t.x - s.x)*sin(theta) + (t.y - s.y)*cos(theta) + s.y

    koch(order - 1, p1, s)
    print("({}, {})\n".format(s.x, s.y))
    koch(order - 1, s, u)
    print("({}, {})\n".format(u.x, u.y))
    koch(order - 1, u, t)
    print("({}, {})\n".format(t.x, t.y))
    koch(order - 1, t, p2)


def main():
    p1 = point(0.0, 0.0)
    p2 = point(100.0, 0)
    order = 1

    print("({}, {})".format(p1.x, p1.y))
    koch(order, p1, p2)
    print("({}, {})".format(p2.x, p2.y))

if __name__ == '__main__':
    main()
