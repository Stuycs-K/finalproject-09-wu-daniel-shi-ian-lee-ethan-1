def string_to_binary(text:str) -> str:
    binary = ''.join(format(i, '08b') for i in bytearray(text, encoding = 'utf-8'))
    return binary

def integer_to_binary(number:int, bits:int = -1) -> str:
    if bits == -1:
        return bin(number)[2:]  # Remove the "0b" prefix
    else:
        binary = bin(number)[2:]
        if (len(binary) < bits):
            return '0' * (bits - len(binary)) + binary
        else:
            return binary[len(binary) - bits:len(binary)]

def get_next_multiple_of_512(num: int) -> int:
    """
    If num is already a multiple of 512, this will just return num
    """
    next_int = 512
    while (next_int < num):
        next_int += 512
    return next_int

def bit_not(binary_string):
    integer_representation = int(binary_string, 2)
    return integer_to_binary(integer_representation, len(binary_string))

def bit_add(binary_string_1, binary_string_2):
    integer_sum = int(binary_string_1, 2)+int(binary_string_2,2)
    return integer_to_binary(integer_sum, 32)

def bit_xor(binary_string_1, binary_string_2):
    if len(binary_string_1)!=len(binary_string_2): raise ValueError("arguments must be same length")
    return integer_to_binary(int(binary_string_1, 2) ^ int(binary_string_2), len(binary_string_1))

def bit_and(binary_string_1, binary_string_2):
    if len(binary_string_1)!=len(binary_string_2): raise ValueError("arguments must be same length")
    return integer_to_binary(int(binary_string_1, 2) & int(binary_string_2), len(binary_string_1))

def right_rotate(binary_string, rotation):
    return binary_string[-rotation:]+binary_string[:len(binary_string)-rotation]

def right_shift(binary_string,rotation) -> str:
    return ('0' * rotation) + binary_string[:len(binary_string)-rotation]
