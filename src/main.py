from sha256 import sha256

#unhashed = input("blah blah blah")
#print(sha256(unhashed))
print(sha256("abc"))
assert(sha256("abc"))=='ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad'
print(sha256("hello"))
assert(sha256("hello"))=='2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
print(sha256(""))
assert(sha256(""))=='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
