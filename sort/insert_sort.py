'''Select Sort
1. Draw cards similar to poker
2. Take the first card in your hand, and draw another card. 
3. Check whether the subscript is valid and compare the card size. If the 
conditions are met, move the card (array shift) and insert the touched card 

Time Complexity: O(n**2)
'''
def insert_sort(arr):
    for i in range(1, len(arr)):
        # touched card
        key = arr[i]
        # index of card in hand
        j = i - 1
        
        # check index and compare 
        while j >= 0 and arr[j] > key:
            # array shift
            arr[j + 1] = arr[j] 
            j = j - 1
        # insert card
        arr[j + 1] = key
    
    return arr

arr = insert_sort([6, 4, 3, 7, 5, 4 ,8])
