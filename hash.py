import hashlib

x = input("Password: ").strip()
hash_hex = hashlib.sha256(x.encode()).hexdigest()
print("hash:", hash_hex)
