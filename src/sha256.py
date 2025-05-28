from util import *

def preprocessing(text) -> str:
    binary = string_to_binary(text)
    message_length = len(binary)

    target_length = get_next_multiple_of_512(message_length + 1 + 64)

    num_padding_zeros = target_length - message_length - 64 - 1
    binary += '1'
    binary += ('0' * num_padding_zeros)

    binary += format(message_length, '064b')

    return binary

def singular_32_split(processed_bits): #split a 512 block into 16 32 bits
    bitArray = []
    for i in range(0, len(processed_bits), 32):
        bitArray.append(processed_bits[i:i+32])
    for i in range(0, 48):
        bitArray.append('0'*32)
    return bitArray

def multiple_32_split(bitArray):
    split_Array=[]
    for i in range(0,len(bitArray)):
        split_Array.append(singular_32_split(bitArray[i]))
    return split_Array



