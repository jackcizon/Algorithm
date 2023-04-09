'''
    why call 'shell'?

    Shell sort is named after its inventor, 
    Donald Shell, who first proposed the algorithm in 1959.
'''

def shell_sort(arr, div):
    n = len(arr)
    gap = n // div
    while gap > 0:
        for i in range(gap, n):
            key = arr[i]
            #start from 0 to grap
            j = i - gap
            while j >= 0 and arr[j] > key:
                arr[j + gap] = arr[j]
                j -= gap
            #arr[j - gap + gap] = key
            arr[j + gap] = key
        gap //= div
    print(arr)

shell_sort([8, 3, 1, 5, 6, 4, 7, 2], 2)

'''
\          \ 
 \    +gap  \ 
  \   ===>>  \ 
   \          \ 
    \          \ 

divided by div
\   \ 
 \   \     +gap//div
  \   \    
   \   \ 

   .....
   .....
final
gap = 1, and compare adjacent element
\\
 \\
  \\
   \\
   ......
            \\

    sort over.
''' 
