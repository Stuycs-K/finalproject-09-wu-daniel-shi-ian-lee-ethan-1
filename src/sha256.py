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


# The next thing to discuss is “rightrotate”. This means we take a binary number, then take its digit on the far right and place it on the far left of the number. Repeat this for the number of times indicated after the word “rightrotate”.

# Now consider “rightshift”. This means removing the digit on the far right and adding a zero to the far left. Repeat this for the number of times indicated.




def rightrotate(text,c) -> str:
    s = ""
    for (i in c):
        s.append(text.charAt(len(text)-i))

    return s+text.substring(len(text)-c)

def rightshift(text,c) -> str:
    