# Your goal is to write a program to convert a base 10 number to its binary representation.
# 1st stage convert an 8 bit number (0 - 128) to binary.
# 2nd stage convert a 16 bit number (0 - 65536) to binary.
import math

def binary_conversion(integer_number):
    if integer_number == 0:
        return 0

    binary_digits = [0] * 16

    exponent = math.floor(math.log(integer_number, 2))

    for i in range(-1, exponent):
        new_number = integer_number - 2 ** exponent

        if new_number >= 0:
            binary_digits[exponent] = 1
            integer_number = new_number

        exponent -= 1

    binary_digits.reverse()
    return "".join(map(str, binary_digits))

        

print(binary_conversion(32788))


# binary_digits = {
#         0: 0,
#         2: 0,
#         4: 0,
#         8: 0,
#         16: 0,
#         32: 0,
#         64: 0,
#         128: 0,
#         256: 0,
#         512: 0,
#         1024: 0,
#         2048: 0,
#         4096: 0,
#         8192: 0,
#         16384: 0,
#         32768: 0,
#         65536: 0
#     }