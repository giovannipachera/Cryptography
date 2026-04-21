import hashlib
import os

def main():
    # Test compute_hashes
    hashes = compute_hashes(b"hello")
    assert hashes["SHA-256"] == hashlib.sha256(b"hello").hexdigest()
    print("✓ compute_hashes corretto")
    for name, digest in hashes.items():
        print(f"  {name:8}: {digest}")

    # Test avalanche
    print("\n--- Avalanche Effect ---")
    demonstrate_avalanche(b"hello", b"hellO")

    # Test birthday paradox
    print("\n--- Birthday Paradox (16 bit) ---")
    attempts = birthday_paradox_demo(16)
    print(f"Collisione trovata in {attempts} tentativi (attesi ~256)")

    # Test preimage resistance
    print("\n--- Preimage Resistance (mini proof-of-work) ---")
    demonstrate_preimage_resistance("000")

def compute_hashes(message: bytes) -> dict:
    return {
        "MD5":     hashlib.md5(message).hexdigest(),
        "SHA-1":   hashlib.sha1(message).hexdigest(),
        "SHA-256": hashlib.sha256(message).hexdigest(),
        "SHA-512": hashlib.sha512(message).hexdigest(),
    }

def demonstrate_avalanche(msg1: bytes, msg2: bytes) -> None:
    h1 = hashlib.sha256(msg1).hexdigest()
    h2 = hashlib.sha256(msg2).hexdigest()

    print(f"  msg1: {msg1}  →  {h1}")
    print(f"  msg2: {msg2}  →  {h2}")

    diff_bits = bin(int(h1, 16) ^ int(h2, 16)).count('1')
    print(f"  Bit diversi: {diff_bits}/256 ({diff_bits/256*100:.1f}%)")

def birthday_paradox_demo(bits: int) -> int:
    seen = {}
    attempts = 0

    while True:
        random_input = os.urandom(8)
        # Tronchiamo SHA-256 a 'bits' bit per simulare hash corto
        full_hash = hashlib.sha256(random_input).digest()
        truncated = int.from_bytes(full_hash[:bits//8], 'big') % (2**bits)

        if truncated in seen:
            print(f"  Collisione: {random_input.hex()} e {seen[truncated].hex()} → stesso hash {truncated}")
            return attempts
        seen[truncated] = random_input
        attempts += 1

def demonstrate_preimage_resistance(target_prefix: str) -> int:
    attempts = 0
    while True:
        random_input = os.urandom(8)
        h = hashlib.sha256(random_input).hexdigest()
        attempts += 1
        if h.startswith(target_prefix):
            print(f"  Trovato in {attempts} tentativi!")
            print(f"  Input: {random_input.hex()}")
            print(f"  Hash:  {h}")
            return attempts


if __name__ == "__main__":
    main()
