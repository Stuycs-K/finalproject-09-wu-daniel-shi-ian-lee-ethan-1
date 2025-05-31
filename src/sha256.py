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
    a=integer_to_binary(HashValues.h0.value,32)
    b=integer_to_binary(HashValues.h1.value,32)
    c=integer_to_binary(HashValues.h2.value,32)
    d=integer_to_binary(HashValues.h3.value,32)
    e=integer_to_binary(HashValues.h4.value,32)
    f=integer_to_binary(HashValues.h5.value,32)
    g=integer_to_binary(HashValues.h6.value,32)
    h=integer_to_binary(HashValues.h7.value,32)
    #STARTING a-h values match h0-h7
    for i in range(64):
        S1=tXor(tXor(rightrotate(e,6),rightrotate(e,11)),rightrotate(e,25))
        ch=tXor(tAnd(e,f),tAnd(tNot(e),g))
        temp1=bitAdd(bitAdd(bitAdd(bitAdd(h,S1),ch),format((RoundConstants.k.value)[i],'b')),str(w[i]))
        SO=tXor(tXor(rightrotate(a,2),rightrotate(a,13)),rightrotate(a,22))
        maj=tXor(tXor(tAnd(a,b),tAnd(a,c)),tAnd(b,c))
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
    s1=""
    for i in range(len(s)):
        if s[i]=="0":
            s1+="1"
        else: s1+="0"
    return s1
#####COMPRESSION######
def bitAdd(s1,s2):
    binary=format((int(s1, 2)+int(s2,2)),'b')
    if len(binary)<32:
        return '0'*(32-len(binary))+binary
    if len(binary)==32:
        return binary
    else: return binary[-32:]
def rightrotate(text,c) -> str:
    return text[-c:]+text[:len(text)-c]

def rightshift(text,c) -> str:
    s=""
    for x in range(c):
        s=s+("0")
    return s + text[:len(text)-c]

def tXor(s1,s2):
    s3=""
    if len(s1)!=len(s2):return "ERROR SHOULD BE EQUAL LENGTHS"
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            s3+='0'
        else: s3+='1'
    return s3

def tAnd(s1,s2):
    s3=""
    if len(s1)!=len(s2):return "ERROR SHOULD BE EQUAL LENGTHS"
    for i in range(len(s1)):
        s3+=compare(s1[i],s2[i])
    return s3

def compare(c1,c2):
    if (c1=='0' and c2=='0'):return '0'
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
