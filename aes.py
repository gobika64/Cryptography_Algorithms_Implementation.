from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

key = get_random_bytes(16)  # AES-128

def encrypt(message):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return base64.b64encode(cipher.nonce + ciphertext).decode()

def decrypt(enc_message):
    data = base64.b64decode(enc_message)
    nonce = data[:16]
    ciphertext = data[16:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(ciphertext).decode()

msg = "Secure Data Communication"
encrypted = encrypt(msg)
decrypted = decrypt(encrypted)

print("Original:", msg)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
