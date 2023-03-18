def mode(a):
    b = []
    c = 1
    k = 0
    for i in range(len(a) - 1):
        max = 0
        mode_num = 0
    
        for j in range(i + 1, len(a)):
    
            if a[i] == a[j]:
                mode_num += 1
        
        #inc arr, 
        if mode_num > max and mode_num != 0:
            k = 0
            max = mode_num
            b[k] = a[i]
            k += 1

        elif mode_num == max:
            b[k] = a[i]
            k +=1

    for i in range(len(a)):
        if a[i] == b[i]:
            c += 1

        if c == len(a):
            print("no mode")

        else:
            print("mode = ")
            print(b)


a = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8]
b = []

mode(a)