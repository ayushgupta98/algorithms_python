arr = [1,2,3,7,3,2]

"""
# Approach 1: Brute-force approach
# Complexity: n-squared
"""
def ispresent(arr, a):
    if a in arr:
        return 1
    else:
        return 0

passed_entries = []
entries_count = []
for i in range(0, len(arr)):
    if ispresent(passed_entries, arr[i]) == 0:
        passed_entries.append(arr[i])
        entries_count.append(1)
    else:
        entries_count[passed_entries.index(arr[i])] += 1 


for i in range(len(entries_count)):
    if entries_count[i] == 1:
        print("Methid 1: Non-repeating entry ", passed_entries[i])


"""
# Approach 2: Hash Map
# Complexity: O(n)
# For this approach to work the pre-requisite is to have all positive number in the array. The downside of using this approach is to have extra memory requirement.
"""
entries_count = [0]*(max(arr)+1)
for i in range(len(arr)):
    entries_count[arr[i]] += 1

for i in range(len(entries_count)):
    if entries_count[i] == 1:
        print("Method 2: Non-repeating entry ", i)
        
    
"""
# Approach 3: Using XOR operation
# Complexity: O(n)
# This is the best possible method to find a non-repeated entry in an array.
# Downside of this method is that this method can find atmost 2 non-repeated enteries in a list.
"""
import math
def getFirstSetBitPos(n):
    return int(math.log2(n&-n)+1)

xor = 0
for i in range(len(arr)):
    xor ^= arr[i]

index = getFirstSetBitPos(xor)

grp1 =[]
grp2 = []

for i in range(len(arr)):
    x = (arr[i])>>(index-1)    
    if x%2 == 1:
        grp1.append(arr[i])
    else:
        grp2.append(arr[i])

result = []
r = 0
for i in range(len(grp1)):
    r ^= grp1[i]
print("Method 3: Non-repeating entry is ", r)

r = 0
for i in range(len(grp2)):
    r ^= grp2[i]
print("Method 3: Non-repeating entry is ", r)
