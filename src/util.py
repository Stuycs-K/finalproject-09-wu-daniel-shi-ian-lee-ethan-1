import typing

def string_to_binary(text:str) -> str:
    binary = ''.join(format(i, '08b') for i in bytearray(text, encoding = 'utf-8'))
    return binary

def get_next_multiple_of_512(num: int) -> int:
    """
    If num is already a multiple of 512, this will just return num
    """
    next_int = 512
    while (next_int < num):
        next_int += 512
    return next_int

def get_512_bit_chunks(binary:str) -> typing.List[str]:
    if (len(binary) % 512 != 0):
        raise ValueError('size of binary should be a multiple of 512')
    total_chunks = int(len(binary) / 512)
    chunks = [''] * total_chunks
    for i in range(total_chunks):
        chunks[i] = binary[(i*512):((i+1)*512)]
    return chunks
    
