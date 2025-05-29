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

def message_schedule(split_Array): 
    for i in range(16, len(split_Array)):
        s0



# The next thing to discuss is “rightrotate”. This means we take a binary number, then take its digit on the far right and place it on the far left of the number. Repeat this for the number of times indicated after the word “rightrotate”.

# Now consider “rightshift”. This means removing the digit on the far right and adding a zero to the far left. Repeat this for the number of times indicated.



#####COMPRESSION######

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
