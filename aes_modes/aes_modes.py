from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def main():
    key = os.urandom(16)

    msg = b"YELLOW SUBMARINEYELLOW SUBMARINE"
    ct_ecb = encrypt_ecb(msg, key)
    assert ct_ecb[:16] == ct_ecb[16:]

    ct_ctr = encrypt_ctr(msg, key)
    assert ct_ctr[:16] != ct_ctr[16:]
    
    demonstrate_ecb_weakness(key)

# ECB: same plaintext = same encryption
def encrypt_ecb(plaintext: bytes, key: bytes):
    cipher = AES.new(key, AES.MODE_ECB)

    if len(plaintext) % 16 != 0:
        padded_plaintext = pad(plaintext, 16)
    else:
        padded_plaintext = plaintext
    
    ct = cipher.encrypt(padded_plaintext)

    return ct

# CTR: same plaintext = different encryption
def encrypt_ctr(plaintext: bytes, key: bytes):
    cipher = AES.new(key, AES.MODE_CTR)
    
    ct = cipher.encrypt(plaintext)

    return ct

def demonstrate_ecb_weakness(key: bytes):
    msg = b"YELLOW SUBMARINEYELLOW SUBMARINE"

    print("ECB:")
    print(encrypt_ecb(msg, key))

    print("\nCTR:")
    print(encrypt_ctr(msg, key))

if __name__ == "__main__":
    main()

