import math

def decimal_convert(decimal, base):
        count = 0
        
        arr = [0 for i in range(32)]

        while decimal > 0:
            rem = decimal % base
            decimal = (int)(decimal / base)
            arr[count] = rem
            count += 1
        
        for i in range(count - 1, -1, -1):
            print(arr[i],end="")

        return arr

decimal_convert(16, 2)


def alpha_to_num(i):
    switcher = {
        'A' : 10,
        'B' : 11,
        'C' : 12,
        'D' : 13,
        'E' : 14,
        'F' : 15
    }
    
    func = switcher.get(i)

    return func


def convert_to_decimal(number, n_base):
    decimal = 0
    count =  0

    arr = [0 for i in range(32)]

    if (int)(n_base) > 10 and n_base < 17:

        for i in range(len(number) - 1, -1, -1):
            
            if number[i].isalpha():
                arr[i] = (int)(alpha_to_num(number[i]))
                count += 1

            elif number[i].isdigit():
                arr[i] = (int)(number[i])
                count += 1

            else:
                pass

        for i in range(count):
            decimal += arr[i] * pow(n_base, count - 1 - i)

        print(decimal)

        return decimal

    else:

        while number > 0:
            rem = number % 10
            number = (int)(number / 10)
            decimal += rem * pow(n_base, count)
            count += 1

        print(decimal)

        return decimal


convert_to_decimal(10000, 2)

convert_to_decimal(77, 8)