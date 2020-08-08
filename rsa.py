def gcd(qn):
    """
    find a minimum number which does not have any common factors with qn other than 1
    """
    for i in range(1, qn):
        if (qn % i != 0):
            break
    return i


def power_split(m, e, n, s):
    """
    Find solution of equation (m^e)%n by splitting e in multiples of 2
    :return: solution of above equation
    """
    power = int(e/s)
    number = pow(m, s, n)
    product_of_remainder = pow(number, power, n)

    remaining = e % s
    remaining_part = pow(m, remaining,n)
    remainder = remaining_part * product_of_remainder
    return remainder%n


p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))
m = input("Enter the value of M: ")
print("Input message is : ")

n = p*q
qn = (p-1)*(q-1)
e = gcd(qn)

print("The value of n is: ", n)
print("The value of qn is: ", qn)
print("The value of e is: ",e)

i = 0
while (True):
    if (i*qn)%e == e-1:
        d = int((i*qn+1)/e)
        break
    i = i + 1

print("The value of d is : ",d)

mssg_list = []
cipher_list = []
for c in m:
    mssg_list.append(ord(c))
    cipher_list.append(power_split(ord(c), e, n, 2))

#print("cipher_list: ", cipher_list)

rx_list = []
for item in cipher_list:
    rx_list.append(chr(power_split(item, d, n, 2)))

rx_string = "".join(rx_list)
print("Message :", mssg_list)
print("Cipher Text: ", cipher_list)
print("RX Text is: ", rx_string)
