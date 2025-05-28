from util import *
from constants import *

def preprocessing(text) -> str:
    binary = string_to_binary(text)
    message_length = len(binary)

    target_length = get_next_multiple_of_512(message_length + 1 + 64)

    num_padding_zeros = target_length - message_length - 64 - 1
    binary += '1'
    binary += ('0' * num_padding_zeros)

    binary += format(message_length, '064b')

    return binary

def get_512_bit_chunks(binary:str) -> typing.List[str]:
    if (len(binary) % 512 != 0):
        raise ValueError('size of binary should be a multiple of 512')
    total_chunks = int(len(binary) / 512)
    chunks = [''] * total_chunks
    for i in range(total_chunks):
        chunks[i] = binary[(i*512):((i+1)*512)]
    return chunks

def concatenate_final_hash_as_binary(h0:int = HashValues.h0, h1:int = HashValues.h1, h2:int = HashValues.h2, h3:int = HashValues.h3, h4:int = HashValues.h4, h5:int = HashValues.h5, h6:int = HashValues.h6, h7:int = HashValues.h7) -> str:
    return integer_to_binary(h0, 8) + integer_to_binary(h1, 8) + integer_to_binary(h2, 8) + integer_to_binary(h3, 8) + integer_to_binary(h4, 8) + integer_to_binary(h5, 8) + integer_to_binary(h6, 8) + integer_to_binary(h7, 8)

def concatenate_final_hash_as_hex() -> str:
    decimal_value = int(concatenate_final_hash_as_binary(), 2)
    hex_string = hex(decimal_value)[2:]
    return hex_string