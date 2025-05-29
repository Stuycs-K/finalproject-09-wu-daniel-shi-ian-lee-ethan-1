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
        temp1=bitAdd(bitAdd(h,S1),ch)+RoundConstants.k[i]+w[i]
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
