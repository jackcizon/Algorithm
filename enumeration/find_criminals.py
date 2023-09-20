'''
1. At least one of a and b has committed a crime;
2. At least 2 of a, e, and f have committed a crime;
3. a and d cannot be co-defendants;
4. b and c may have committed the crime.
5. Only one person in c and d committed the crime.
6. If d did not participate in the crime, then e cannot participate in the crime.

Based on the above discussion, find the criminals among 'a to f'
'''


class CriminalFinder:
    def __init__(self):
        self.criminal_combinations = []

    def check_conditions(self, a, b, c, d, e, f):
        # Condition 1: At least one of a and b has committed a crime
        condition1 = a or b

        # Condition 2: At least 2 of a, e, and f have committed a crime
        a_ef_count = a + e + f
        condition2 = a_ef_count >= 2

        # Condition 3: a and d cannot be co-defendants
        condition3 = not (a and d)

        # Condition 4: b and c may have committed the crime
        # Condition 5: Only one person in c and d committed the crime
        condition4 = (b and c) or (c and not d) or (d and not c)

        # Condition 6: If d did not participate, then e cannot participate
        condition6 = not (not d and e)

        return condition1 and condition2 and condition3 and condition4 and condition6

    def find_criminals(self):
        for a in [True, False]:
            for b in [True, False]:
                for c in [True, False]:
                    for d in [True, False]:
                        for e in [True, False]:
                            for f in [True, False]:
                                if self.check_conditions(a, b, c, d, e, f):
                                    self.criminal_combinations.append({
                                        'a': a, 
                                        'b': b, 
                                        'c': c, 
                                        'd': d, 
                                        'e': e, 
                                        'f': f})

    def print_criminal_combinations(self):
        if len(self.criminal_combinations) > 0:
            print("Possible criminal combinations:")
            for idx, combination in enumerate(self.criminal_combinations, start=1):
                criminals = [person for person, is_criminal in combination.items() if is_criminal]# key: val
                print(f"Combination {idx}: {' '.join(criminals)}")
        else:
            print("No possible criminal combinations found.")


# Create an instance of the CriminalFinder class
criminal_finder = CriminalFinder()
criminal_finder.find_criminals()
criminal_finder.print_criminal_combinations()
