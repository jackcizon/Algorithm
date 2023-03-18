def _charge(sorted_arr_dec, charge, arr_count):
    for i in range(len(sorted_arr_dec)):
        arr_count[i] = 0

        while charge >= sorted_arr_dec[i]:
            arr_count[i] += 1
            temp = charge
            charge -= sorted_arr_dec[i]
        
            print("take {} ${} from {} remain {}"
                .format(1, sorted_arr_dec[i], temp, charge))
    
    print("\nsum:")
    
    for i in range(len(arr_count)):
    
        if arr_count[i] != 0:
            print("take {} ${}"
                .format(arr_count[i], sorted_arr_dec[i]))


sorted_arr_dec = [50, 40, 25, 15, 10, 5, 2, 1]

charge = 189

arr_count = [0 for i in range(len(sorted_arr_dec))]

_charge(sorted_arr_dec, charge, arr_count)
