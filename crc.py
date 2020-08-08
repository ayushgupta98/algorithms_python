px = input('Enter Message Polynomial: ')
gx = input('Enter Generator Polynomial: ')

to_append = len(gx) - 1
original_px = px
for i in range(to_append):
    px = '{0}0'.format(px)


def filter_px(px):
    """
    This function is used to remove the zero from the MSB bit.
    :param px: unfiltered polynomial
    :return: filtered polynomial
    """
    if px[0] == '0':
        return px[1:]


def binary_division(px, gx):
    """
    This function divides two polynomial using binary operations
    :param px: Dividend polynimial
    :param gx: Divisor polynomial
    :return: Remainder polynimial
    """
    while len(px) >= len(gx):
        while px[0] == '0':
            px = filter_px(px)
            if len(px) < len(gx):
                return px

        for i in range(0, len(gx)):
            if gx[i] == px[i]:
                s = list(px)
                s[i] = '0'
                px = "".join(s)
            else:
                s = list(px)
                s[i] = '1'
                px = "".join(s)
    return px


crc = binary_division(px, gx)
print("CRC code: ", crc)

new_px = original_px + crc
print("New px: ", new_px)

remainder = binary_division(new_px, gx)
print("Remainder: ", remainder)
