from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

cipher_rsa = PKCS1_OAEP.new(public_key)
encrypted = cipher_rsa.encrypt(b"Cyber Security Internship")

cipher_rsa_dec = PKCS1_OAEP.new(private_key)
decrypted = cipher_rsa_dec.decrypt(encrypted)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted.decode())
