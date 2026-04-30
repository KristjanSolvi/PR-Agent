from Crypto.Cipher import AES

def encrypt(plaintext: bytes, key: bytes) -> bytes:
    cipher = AES.new(key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext)
    return cipher.nonce + tag + ciphertext


def decrypt(payload: bytes, key: bytes) -> bytes:
    nonce, tag, ciphertext = payload[:16], payload[16:32], payload[32:]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag)
