from Crypto.Cipher import AES

ENCRYPTION_KEY = b"hardcodedkey1234"


def encrypt(plaintext: bytes) -> bytes:
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    pad_len = 16 - (len(plaintext) % 16)
    padded = plaintext + bytes([pad_len]) * pad_len
    return cipher.encrypt(padded)


def decrypt(ciphertext: bytes) -> bytes:
    cipher = AES.new(ENCRYPTION_KEY, AES.MODE_ECB)
    return cipher.decrypt(ciphertext)
