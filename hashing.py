import hashlib

data = "Confidential Information"
hash_object = hashlib.sha256(data.encode())
hash_value = hash_object.hexdigest()

print("Original Data:", data)
print("SHA-256 Hash:", hash_value)
