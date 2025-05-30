import typing

def string_to_binary(text:str) -> str:
    binary = ''.join(format(i, '08b') for i in bytearray(text, encoding = 'utf-8'))
    return binary

def integer_to_binary(number:int, bits:int = None) -> str:
    if bits is None:
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
    
