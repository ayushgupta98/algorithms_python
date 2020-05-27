
def merge_sort(arr):    
    """
    The complexity of this merge_sort is nlogn.
    """
    n = len(arr)
    if n == 1:
        return arr

    c = [0]*n
    a, b = [], []
    if n%2 == 1:
        a = arr[0:(int(n/2)+1)]
        b = arr[(int(n/2)+1):]
    else:
        a = arr[0:(int(n/2))]
        b = arr[(int(n/2)):]
        
    i, j = 0, 0
    a = merge_sort(a)
    b = merge_sort(b)

    n1 = len(a)
    n2 = len(b)

    for k in range(n):    
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
        elif a[i] > b[j]:
            c[k] = b[j]
            j += 1
            
        if i == n1:
            for s in range(j, n2):
                k += 1
                c[k] = b[s] 
            break
        if j == n2:
            for s in range(i, n1):
                k += 1
                c[k] = a[s]
            break
    return c



arr = [43, 19, 11,8,1,3,4,5,2,7,6, 10, 14, 0, 23]
print(merge_sort(arr))
