# Dev Log:

This document must be updated daily every time you finish a work session.

## Ian Shi

### 05/20/25 - Learning Sha256
Did research on how SHA256 works and the steps it takes to hash something with this algorithm.

### 05/22/25 - Constants and README
Added constants required for the SHA256 hashing algorithm.
These constants represent the first 32 bits of the fractional parts of the square roots of the first 8 primes
and the first 32 bits of the fractional parts of the cube roots of the first 64 primes.

Updated and formatted README

### 05/23/25 - Test cases and simplification
Added test cases
More abstraction
Simplified preprocessing step

### 05/24/25 - Fix preprocessing, add test cases for preprocessing
As the name implies...

### 5/27/25 - Step 4 (breaking into chunks)
wrote get_512_bit_chunks(), which converts the binary into a array of parts which each has 512 bits
wrote test cases for it

### 5/28/25 - Step 8 (Concatenate final hash)
wrote concatenate_final_hash_as_binary() and concatenate_final_hash_as_hex()
wrote test cases

### 5/29/25 - 6/2/25 - Helped other group members
mainly helped with step 5 and 6 (message schedule and compression)

### 6/3/25 - Finished SHA256
Fixed edge cases, working SHA256
wrote test cases