from math import ceil, floor

def karatsuba_multiplier(x,y):
    if x < 10 and y < 10: # recussion termination condition
        return x*y

    n = max(len(str(x)), len(str(y)))
    m = ceil(n/2)   

    a  = floor(x / 10**m)
    b = x % (10**m)

    c = floor(y / 10**m)
    d = y % (10**m)

    #recursive calls
    ac = karatsuba_multiplier(a,c)
    bd = karatsuba_multiplier(b,d)
    guass_trick = karatsuba_multiplier(a+b, c+d) - ac - bd

    return int(ac*(10**(m*2)) + guass_trick*(10**m) + bd)





a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = karatsuba_multiplier(a,b)
print(result)
print(a*b)

if a*b == result:
    print("Correct")
else:
    print("Incorrect")

