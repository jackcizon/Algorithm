'''
    According to Fermat's Last Theorem, 
    no three positive integers a, b, c satisfy the equation, 
    a^n + b^n = c^n    for any integer value of n greater than 2. 
    For n = 1 and n = 2, 
    the equation have infinitely many solutions.

    a != y != z
'''

def fermat_last_theorem_test(domain, n):
    if n < 3:
        return
    
    for a in range(1, domain + 1):

        for b in range(a, domain + 1):
            #we can from 1 to domain, but some loops are repeat
            pow_sum = pow(a, n) + pow(b, n)
            c = pow(pow_sum, 1.0 / n)
            c_pow = pow(int(c), n)

            if c_pow == pow_sum:
                print("{}^n + {}^n = {}^n",
                format(a, b, c))

    print("not found")
        

fermat_last_theorem_test(100, 5)