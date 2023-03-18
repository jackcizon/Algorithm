'''
    mappping :
        M => 1000
        D => 500 
        C => 100 
        L => 50 
        X => 10 
        V => 5 
        I => 1        
'''


def decimal_to_roman(number):
    roman = ''
    decimal_map = [1000,  900, 500,  400, 100,   90,  50,   40,  10,    9,   5,    4,  1]
    roman_map =   [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    for i in range(len(decimal_map)):

        while number >= decimal_map[i]:
            roman += roman_map[i]
            number -= decimal_map[i]

    return roman
    

def main():
    roman = decimal_to_roman(1978)
    print(roman)


if __name__ == '__main__':
    main()
    