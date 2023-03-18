# Program to convert Roman
# Numerals to Numbers
roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000 
    }

def romanToInt(s):
    
    sum = 0
    i = 0

    while i < len(s) :

        if (i != len(s) - 1 and roman[s[i]] < roman[s[i + 1]]):
            sum += roman[s[i + 1]] - roman[s[i]]
            i += 2

            continue

        else:
            sum += roman[s[i]]
        i += 1

    return sum


input = "MCMIV"

print(f"Integer form of Roman Numeral is {romanToInt(input)}")

