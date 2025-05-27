# Dev Log:

This document must be updated daily every time you finish a work session.

## Daniel Wu

### 2025-05/20/25 - Learning Sha256
We conducted research on the SHA-256 algorithm, how to encode it, and what happens if we decode it. In our research, we found that only the encoder for SHA exists, but no decoder. At first we tried simple messages to encrypt with SHA and tried decoding them, which worked for basic messages, but failed for complex ones. We then determined that SHA only has an encoder, not a decoder. ~ 1 hour

### 2024-05/22/25 - Preprocessing
I am currently working on the preprocessing of bits of SHA256, currently trying to understand how to round the bit count to the multiples of 512. I got the preprocessing of the binary values to work, in which I had to first convert the message into binary string format, then count the length of the binary, find the closest multiple of 512 that it rounds up to, which has a caveat in that enough space has to be reserved for a 64 bit section and a number 1 bit, and pad additional zeroes as needed.

### 2024-01-03 - Brief description

### 2024-01-03 - Brief description

### 2024-01-03 - Brief description

### 2024-01-03 - Brief description

