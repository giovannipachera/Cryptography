import hmac, hashlib, os

def main():
    key = os.urandom(32)
    msg = b"Transfer 1000 euros to Bob"

    tag = compute_hmac(msg, key)
    assert verify_hmac(msg, key, tag) == True
    assert verify_hmac(b"Transfer 9000 euros to Bob", key, tag) == False
    assert verify_hmac(msg, os.urandom(32), tag) == False

    demonstrate_integrity(msg, key)
    
    return 0

def compute_hmac(message: bytes, key: bytes) -> str:
    h = hmac.new(key, message, hashlib.sha256)
    
    return h.hexdigest()

def verify_hmac(message: bytes, key: bytes, tag: str) -> bool:
    h = compute_hmac(message, key)

    return hmac.compare_digest(h, tag)

def demonstrate_integrity(message: bytes, key: bytes) -> None:
    h = compute_hmac(message, key)

    verify_hmac(message, key, h)

    tamper_message = bytearray(message)
    tamper_message[0] = os.urandom(1)[0]

    verify_hmac(tamper_message, key, h)

    tamper_key = bytearray(key)
    tamper_key[0] = os.urandom(1)[0]

    verify_hmac(message, tamper_key, h)

if __name__ == "__main__":
    main()
    


