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
    rr7 = rightrotate(binary_string,7)
    rr18 = rightrotate(binary_string, 18)
    rs3 = rightshift(binary_string, 3)
    xor1 = tXor(rr7, rr18)
    xorfinal = tXor(xor1, rs3)
    return xorfinal

def s1(binary_string):
    rr17 = rightrotate(binary_string, 17)
    rr19 = rightrotate(binary_string, 19)
    rs10 = rightshift(binary_string, 10)
    xor = tXor(rr17, rr19)
    xorfinal = tXor(xor, rs10)
    return xorfinal

def message_schedule(split_array):
    for i in range(16, len(split_array)):
        s0value = s0(split_array[i-15])
        s1value = s1(split_array[i-2])
        sum = (split_array[i-16] + s0value) % (2**32)
        sum = (sum + split_array[i-7]) % (2**32)
        return (sum + s1) % (2**32)
    

# The next thing to discuss is “rightrotate”. This means we take a binary number, then take its digit on the far right and place it on the far left of the number. Repeat this for the number of times indicated after the word “rightrotate”.

# Now consider “rightshift”. This means removing the digit on the far right and adding a zero to the far left. Repeat this for the number of times indicated.
def testSha(w):
    a=HashValues.h0
    b=HashValues.h1
    c=HashValues.h2
    d=HashValues.h3
    e=HashValues.h4
    f=HashValues.h5
    g=HashValues.h6
    h=HashValues.h7
    for i in range(63):
        S1=tXor(tXor(rightrotate(e,6),rightrotate(a,11)),rightrotate(e,25))
        ch=tXor(tAnd(e,f),tXor(tAnd((tNot(e)),g)))
        temp1=bitAdd(bitAdd(bitAdd(bitAdd(h,S1),ch),str(RoundConstants.k[i])),str(w[i]))
        SO=tXor(tXor(rightrotate(a,2),rightrotate(a,13)),rightrotate(a,22))
        maj=tXor(tXor(tAnd(a,b),tAnd(a,c)),tXor(b,c))
        temp2=bitAdd(SO,maj)
        h=g
        g=f
        f=e
        e=bitAdd(d,temp1)
        d=c
        c=b
        b=a
        a=bitAdd(temp1,temp2)
    l=[]
    l.append(a)
    l.append(b)
    l.append(c)
    l.append(d)
    l.append(e)
    l.append(f)
    l.append(g)
    l.append(h)
    return l


def tNot(s):
    for i in range(len(s)):
        s[i]=str(not int(s[i]))
    return s
#####COMPRESSION######
def bitAdd(s1,s2):
    return bin((int(s1, 2)+int(s2,2)))[2:]
def rightrotate(text,c) -> str:
    return text[-c:]+text[:len(text)-c]

def rightshift(text,c) -> str:
    s=""
    for x in range(c):
        s=s+("0")
    return s + text[:len(text)-c]

def tXor(s1,s2):
    s3=""
    for i in range(len(s1)):
        s3=s3+str(int(s1[i])^int(s2[i]))
    return s3

def tAnd(s1,s2):
    s3=""
    for i in range(len(s1)):
        s3=s3+compare(s1[i],s2[i])
    return s3

def compare(c1,c2):
    if (c1=='0' and c2=='0'):return '1'
    if (c1=='1' and c2=='0'):return '0'
    if (c1=='0' and c2=='1'):return '0'
    if (c1=='1' and c2=='1'):return '1'
    return 0
def reverse_string(s):
  return s[::-1]
def get_512_bit_chunks(binary:str) -> typing.List[str]:
    if (len(binary) % 512 != 0):
        raise ValueError('size of binary should be a multiple of 512')
    total_chunks = int(len(binary) / 512)
    chunks = [''] * total_chunks
    for i in range(total_chunks):
        chunks[i] = binary[(i*512):((i+1)*512)]
    return chunks

def concatenate_final_hash_as_binary(h0:int = HashValues.h0, h1:int = HashValues.h1, h2:int = HashValues.h2, h3:int = HashValues.h3, h4:int = HashValues.h4, h5:int = HashValues.h5, h6:int = HashValues.h6, h7:int = HashValues.h7) -> str:
    return integer_to_binary(h0, 32) + integer_to_binary(h1, 32) + integer_to_binary(h2, 32) + integer_to_binary(h3, 32) + integer_to_binary(h4, 32) + integer_to_binary(h5, 32) + integer_to_binary(h6, 32) + integer_to_binary(h7, 32)

def concatenate_final_hash_as_hex(h0:int = HashValues.h0, h1:int = HashValues.h1, h2:int = HashValues.h2, h3:int = HashValues.h3, h4:int = HashValues.h4, h5:int = HashValues.h5, h6:int = HashValues.h6, h7:int = HashValues.h7) -> str:
    decimal_value = int(concatenate_final_hash_as_binary(h0, h1, h2, h3, h4, h5, h6, h7), 2)
    hex_string = hex(decimal_value)[2:].zfill(64)
    return hex_string
