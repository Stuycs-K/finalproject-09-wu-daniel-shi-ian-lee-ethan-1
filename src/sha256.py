import typing

from util import *
from constants import *


def sha256(input):
    binaryString = preprocessing(input)
    chunks = get_512_bit_chunks(binaryString)
    for chunk in chunks:
        split_32 = singular_32_split(chunk)
        schedule = message_schedule(split_32)
        compression(schedule)
    return concatenate_final_hash_as_hex()


def preprocessing(text) -> str:
    binary = string_to_binary(text)
    message_length = len(binary)

    target_length = get_next_multiple_of_512(message_length + 1 + 64)

    num_padding_zeros = target_length - message_length - 64 - 1
    binary += '1'
    binary += ('0' * num_padding_zeros)

    binary += format(message_length, '064b')

    return binary

#following functions are per 512 chunk
def singular_32_split(processed_bits): #split a 512 block into 16 32 bits
    bitArray = []
    for i in range(0, len(processed_bits), 32):
        bitArray.append(processed_bits[i:i+32])
    for i in range(0, 48):
        bitArray.append('0'*32)
    return bitArray

def multiple_32_split(chunk_Array):
    split_Array=[]
    for i in range(0,len(chunk_Array)):
        split_Array.append(singular_32_split(chunk_Array[i]))
    return split_Array

#message_schedule helpers

def s0(binary_string):
    rr7 = right_rotate(binary_string,7)
    rr18 = right_rotate(binary_string, 18)
    rs3 = right_shift(binary_string, 3)
    xor1 = bit_xor(rr7, rr18)
    xorfinal = bit_xor(xor1, rs3)
    return xorfinal

def s1(binary_string):
    rr17 = right_rotate(binary_string, 17)
    rr19 = right_rotate(binary_string, 19)
    rs10 = right_shift(binary_string, 10)
    xor = bit_xor(rr17, rr19)
    xorfinal = bit_xor(xor, rs10)
    return xorfinal

def message_schedule(split_array):
    for i in range(16, len(split_array)):
        s0value = s0(split_array[i-15])
        s1value = s1(split_array[i-2])
        sum = bit_add(split_array[i-16], s0value) #(split_array[i-16] + s0value) % (2**32)
        sum = bit_add(sum, split_array[i-7])
        sum = bit_add(sum, s1value)
        split_array[i] = sum #format((int(sum)) % (2**32), 'b')
    return split_array

def compression(w):
    a=integer_to_binary(HashValues.h.value[0],32)
    b=integer_to_binary(HashValues.h.value[1],32)
    c=integer_to_binary(HashValues.h.value[2],32)
    d=integer_to_binary(HashValues.h.value[3],32)
    e=integer_to_binary(HashValues.h.value[4],32)
    f=integer_to_binary(HashValues.h.value[5],32)
    g=integer_to_binary(HashValues.h.value[6],32)
    h=integer_to_binary(HashValues.h.value[7],32)
    #STARTING a-h values match h0-h7
    for i in range(64):
        S1=bit_xor(bit_xor(right_rotate(e,6),right_rotate(e,11)),right_rotate(e,25))
        ch=bit_xor(bit_and(e,f),bit_and(bit_not(e),g))
        temp1=bit_add(bit_add(bit_add(bit_add(h,S1),ch),format((RoundConstants.k.value)[i],'b')),str(w[i]))
        SO=bit_xor(bit_xor(right_rotate(a,2),right_rotate(a,13)),right_rotate(a,22))
        maj=bit_xor(bit_xor(bit_and(a,b),bit_and(a,c)),bit_and(b,c))
        temp2=bit_add(SO,maj)
        h=g
        g=f
        f=e
        e=bit_add(d,temp1)
        d=c
        c=b
        b=a
        a=bit_add(temp1,temp2)

    binaries = [a, b, c, d, e, f, g, h]
    values = []
    for binary in binaries:
        values.append(int(binary, 2))
    for i in range(8):
        HashValues.h.value[i] += values[i]
        HashValues.h.value[i] %= (2 ** 32)
 
def get_512_bit_chunks(binary:str) -> typing.List[str]:
    if (len(binary) % 512 != 0): raise ValueError('size of binary should be a multiple of 512')
    total_chunks = int(len(binary) / 512)
    chunks = [''] * total_chunks
    for i in range(total_chunks):
        chunks[i] = binary[(i*512):((i+1)*512)]
    return chunks

def concatenate_final_hash_as_binary(h0:int = HashValues.h.value[0], h1:int = HashValues.h.value[1], h2:int = HashValues.h.value[2], h3:int = HashValues.h.value[3], h4:int = HashValues.h.value[4], h5:int = HashValues.h.value[5], h6:int = HashValues.h.value[6], h7:int = HashValues.h.value[7]) -> str:
    return integer_to_binary(h0, 32) + integer_to_binary(h1, 32) + integer_to_binary(h2, 32) + integer_to_binary(h3, 32) + integer_to_binary(h4, 32) + integer_to_binary(h5, 32) + integer_to_binary(h6, 32) + integer_to_binary(h7, 32)

def concatenate_final_hash_as_hex(h0:int = HashValues.h.value[0], h1:int = HashValues.h.value[1], h2:int = HashValues.h.value[2], h3:int = HashValues.h.value[3], h4:int = HashValues.h.value[4], h5:int = HashValues.h.value[5], h6:int = HashValues.h.value[6], h7:int = HashValues.h.value[7]) -> str:
    decimal_value = int(concatenate_final_hash_as_binary(h0, h1, h2, h3, h4, h5, h6, h7), 2)
    hex_string = hex(decimal_value)[2:].zfill(64)
    return hex_string