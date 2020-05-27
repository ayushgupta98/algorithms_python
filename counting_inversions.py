
def count_the_inversion_by_brute_force(arr):
    """
    The complexity of this merge_sort is n squared.
    Maximum inversions can occur when the list given is in reverse order.
    Number of maximum inversions for a list of size n is = nC2 = n(n+1)/2
    """
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                count += 1
    print(arr)
    return count



def count_the_inversion_by_merge_sort(arr):    
    """
    The complexity of this merge_sort is nlogn.
    Maximum inversions can occur when the list given is in reverse order.
    Number of maximum inversions for a list of size n is = nC2 = n(n+1)/2
    """
    n = len(arr)
    if n == 1:
        return arr, 0

    c = [0]*n
    a, b = [], []
    if n%2 == 1:
        a = arr[0:(int(n/2)+1)]
        b = arr[(int(n/2)+1):]
    else:
        a = arr[0:(int(n/2))]
        b = arr[(int(n/2)):]
        
    i, j = 0, 0
    a, c1 = count_the_inversion_by_merge_sort(a)
    b, c2 = count_the_inversion_by_merge_sort(b)

    n1 = len(a)
    n2 = len(b)
    count = 0
    for k in range(n):    
        if a[i] < b[j]:
            c[k] = a[i]
            i += 1
        elif a[i] > b[j]:
            c[k] = b[j]
            j += 1
            count += (n1-i)
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
    return c, count+c1+c2



arr = [6,1,3,5,2,4]
print("Number of Inversions to sort the list: ", count_the_inversion_by_brute_force(arr))
arr = [6,1,3,5,2,4]
print("Number of Inversions to sort the list: ", count_the_inversion_by_merge_sort(arr)[1])
