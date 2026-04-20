capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters = "abcdefghijklmnopqrstuvwxyz"

def main():
    assert encrypt("SECURE", 3) == "VHFXUH"
    assert decrypt("VHFXUH", 3) == "SECURE"
    assert encrypt("Hello World", 13) == "Uryyb Jbeyq"  # ROT13!
    
    return 0

# encrypting a plaintext into its respective ciphertext given the key
def encrypt(plaintext: str, key: int):
    ciphertext = ""
    
    for i in plaintext:
        if i in capital_letters:
            ciphertext = ciphertext + capital_letters[(capital_letters.index(i) + key) % len(capital_letters)] 
        elif i in lower_letters:
            ciphertext = ciphertext + lower_letters[(lower_letters.index(i) + key) % len(lower_letters)]
        else:
            ciphertext = ciphertext + i

    return ciphertext

# decrypting a chipertext into its respective plaintext given the key
def decrypt(ciphertext: str, key: int):
    plaintext = ""

    for i in ciphertext:
        if i in capital_letters:
            plaintext = plaintext + capital_letters[(capital_letters.index(i) - key) % len(capital_letters)] 
        elif i in lower_letters:
            plaintext = plaintext + lower_letters[(lower_letters.index(i) - key) % len(lower_letters)]
        else:
            plaintext = plaintext + i

    return plaintext

# brute forceing the decrypting function to retrieve the key
def brute_force(ciphertext: str):
    key = 0

    while(key < len(capital_letters)):
        print("key = " + str(key) + " -> " + decrypt(ciphertext, key))

        key = key + 1


if __name__ == "__main__":
    main()


    
        
    
