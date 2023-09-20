"""
A, B, C, D who is lying.

A: this man is not me -> thisman != 'A'
B: this man is 'C' -> thisman == 'C'
C: this man is 'D' -> thisman == 'D'
D: C is lying -> thisman != 'D'
"""

def check():
    answer = False
    for i in range(0, 4):
        thisman = ord('A') + i
        sum = (thisman != ord('A')) + (thisman == ord('C')) + (thisman == ord('D')) + (thisman != ord('D'))
        if sum == 3:
            print("{} is lying.".format(chr(thisman)), end="\n")
            answer = True
            break
    if not answer:
        print("cannot find who is lying.")

check()
