# Dev Log:

This document must be updated daily every time you finish a work session.

## Daniel Wu

### 2025-05/20/25 - Learning Sha256
We conducted research on the SHA-256 algorithm, how to encode it, and what happens if we decode it. In our research, we found that only the encoder for SHA exists, but no decoder. At first we tried simple messages to encrypt with SHA and tried decoding them, which worked for basic messages, but failed for complex ones. We then determined that SHA only has an encoder, not a decoder. 

### 2024-05/22/25 - Preprocessing
I am currently working on the preprocessing of bits of SHA256, currently trying to understand how to round the bit count to the multiples of 512. I got the preprocessing of the binary values to work, in which I had to first convert the message into binary string format, then count the length of the binary, find the closest multiple of 512 that it rounds up to, which has a caveat in that enough space has to be reserved for a 64 bit section and a number 1 bit, and pad additional zeroes as needed.

### 2024-05/23/25 - 64 Bit
Worked on making the 64-bit at the end of the program, turning the length of the binary of the  we organized our code around, creating a separate sha256.py file in order to have the functions for sha in one place, as well as adding test cases to test the code.

### 2024-05/24/25 - Additional Research
I did additional research on the SHA algorithum and implementation methods.

### 2024-05/27/25 - Message Schedule
Worked on encoding the message  schedule of Sha256

### 2024-05/28/25 - Message Schedule 2
Finished encoding the splitting of the 512 blocks into 16 32 bit strings in arrays for each block

### 2024-05/29/25 - Message Schedule 3
Working on creating the 64-word message schedule
### 2024-01-03 - Brief description

### 2024-01-03 - Brief description

### 2024-01-03 - Brief description


