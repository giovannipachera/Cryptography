import os

def main():
    msg1 = b"Hello Bob"
    msg2 = b"Attack now"
    key  = generate_key(len(msg1))

    ct   = encrypt(msg1, key)
    assert decrypt(ct, key) == msg1

    # key reuse
    k    = generate_key(9)
    ct1  = encrypt(b"Hello Bob", k)
    ct2  = encrypt(b"Nine char", k)
    xor_ct = reuse_attack(ct1, ct2)
    assert xor_ct == bytes(a ^ b for a, b in zip(b"Hello Bob", b"Nine char"))
    
    return 0


# generating encrypted bytes
def generate_key(length: int):
    key = os.urandom(length)

    return key

# encryption based on XOR
def encrypt(plaintext: bytes, key: bytes):
    try:
        ciphertext = bytes(a ^ b for a, b in zip(plaintext, key))
            
    except ValueError:
        print("Different lengths")

    return ciphertext

# decryption based on XOR
def decrypt(ciphertext: bytes, key: bytes):
    try:
        plaintext = bytes(a ^ b for a, b in zip(ciphertext, key))
            
    except ValueError:
        print("Different lengths")

    return plaintext

# prove keys should not be used more than once  
def reuse_attack(ct1: bytes, ct2: bytes):
    p1_XOR_p2 = bytes(a ^ b for a, b in zip(ct1, ct2))

    return p1_XOR_p2

if __name__ == "__main__":
    main()



