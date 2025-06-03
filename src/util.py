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

def bit_not(s):
    s1=""
    for i in range(len(s)):
        if s[i]=="0":
            s1+="1"
        else: s1+="0"
    return s1

def bit_add(s1,s2):
    binary=format((int(s1, 2)+int(s2,2)),'b')
    if len(binary)<32:
        return '0'*(32-len(binary))+binary
    if len(binary)==32:
        return binary
    else: return binary[-32:]

def right_rotate(text,c):
    return text[-c:]+text[:len(text)-c]

def right_shift(text,c):
    s=""
    for x in range(c):
        s=s+("0")
    return s + text[:len(text)-c]

def bit_xor(s1,s2):
    s3=""
    if len(s1)!=len(s2):return "ERROR SHOULD BE EQUAL LENGTHS"
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            s3+='0'
        else: s3+='1'
    return s3

def bit_and(s1,s2):
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
    return '0'
