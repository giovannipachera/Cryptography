import sys
sys.path.append('../caesar_cipher')
from caesar import encrypt, decrypt

def main():
    testo = (
        "In the beginning was the Word and the Word was with God and the Word was God. "
        "The same was in the beginning with God. All things were made by him and without "
        "him was not any thing made that was made. In him was life and the life was the "
        "light of men. And the light shineth in darkness and the darkness comprehended it not."
    )
    secret = encrypt(testo, 7)
    result = attack(secret)
    assert result.lower() == testo.lower()

# stating frequency of each letter in an input string
def letter_frequency(text: str):
    occurences = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}
    frequences = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}

    for i in text:
        if i.upper() in occurences.keys():
            occurences[i.upper()] += 1

    for i in frequences:
        total_letters = sum(occurences.values())
        frequences[i] = occurences[i] / total_letters * 100

    return frequences

# guessing the key
def guess_key(ciphertext: str):
    frequences = letter_frequency(ciphertext)
    max_frequency = max(frequences, key=frequences.get)

    key = (ord(max_frequency) - ord("E"))%26

    return key

# performing attack based on character frequencies
def attack(ciphertext: str):
    key = guess_key(ciphertext)

    plaintext = decrypt(ciphertext, key)

    print("Chiave indovinata: " + str(key))

    return plaintext

if __name__ == "__main__":
    main()
