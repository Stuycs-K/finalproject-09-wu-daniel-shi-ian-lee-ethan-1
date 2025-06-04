
# SHA-256

### SHA-256 Encoding
[Encoding process for SHA-256](https://blog.boot.dev/cryptography/how-sha-2-works-step-by-step-sha-256/) 

### What is SHA-256?
- SHA-256 (Secure Hashing Algorithm 256) is a hashing algorithm that is used to store data securely in the form of an uncrackable hash.

- SHA-256 comes from the SHA-2 family of hash algorithms, successor of the SHA-1 family.

### History of SHA
- SHA originated in the National Security Agency(NSA) in the U.S.  and was implemented as a standard for securing online data in the form of SHA-1, a 160 bit hash.

- However, this hash was susceptible to collision attacks, where two different messages led to the same hash, and the first collision occurred in 2017, when Google and UWI Amsterdam researchers demonstrated this collision vulnerability to the public. [Source: Google](https://security.googleblog.com/2017/02/announcing-first-sha1-collision.html)

- This was done using around 9 quintillion hash computations. Hence, a new algorithm was needed.

### Security of SHA-256
- To this day, SHA-256 is widely regarded as a highly secure hashing algorithms, with no known exploits/vulnerabilities other than brute forcing very short hashed messages.

- This is partly due to the number of bits in the hash, which allows for 2^256 permutations of hashes, leading to unreasonable cracking times for longer original messages.

- To put into context, if you had a supercomputer that could run 4 billion SHA-256 hashes in a second, and a superorganization had 4 billion of those computers, and half of the Earth's population owned such a superorganization, and 4 billion of those Earths in a Milky Way, and 4 billion of the Milky Ways, and gave it about 37x the age of the universe to crack a hash, it would still be a 1 in 4 billion chance for the message to be correct. [(Credit: 3Blue1Brown)] (https://www.youtube.com/watch?v=S9JGmA5_unY)

- However, SHA-256 should not be used for password storage, as it becomes very easy to brute force with password lists or rainbow tables.

### Applications of SHA-256
- Digital signatures: The SHA-256 hash of a message is encrypted with a private key, the receiver decrypts using their key to find the SHA-256 hash, compares it to the hash of the message they received.

- Blockchain: Blockchain is a digital ledger that records transactions in a block chain, with each block being a unique identifier for each transaction. Uses the SHA-256 digital signatures to verify user transactions, and every “block” of a blockchain is added to the previous block and is generated using SHA-256, ensuring the immutability of the chain.

### Unique Characteristics of SHA-256
- 256-bit encoding, making it collision-resistant compared to shorter hashes such as the 128-bit MD5.

- Fast and efficient for its security level, due to its compression function and message schedule working on 32-bit blocks for 64 rounds making it computationally straightforward.

- Relatively impossible cracking time for messages that aren’t small.

### SHA-256 vs SHA-1
- SHA-256 is in the SHA-2 family, a family of hashing algorithms that utilize higher bit counts for extra security.

- The SHA-1 hashing algorithm is fundamentally the same as SHA-256, but instead of having 256 bits in its hash, it has 160 bits.

- Although this means the SHA-1 algorithm is slightly faster than SHA-256, due to its lack of collision resistance and vulnerabilities to brute force attacks, SHA-256’s security outshines its slower performance.

### Sources:
- https://specopssoft.com/blog/sha256-hashing-password-cracking/
- https://security.googleblog.com/2017/02/announcing-first-sha1-collision.html
- https://www.simplilearn.com/tutorials/cyber-security-tutorial/sha-256-algorithm
- https://www.encryptionconsulting.com/education-center/sha-256/
- https://www.securew2.com/blog/what-is-sha-encryption-sha-256-vs-sha-1




