import hashlib
import secrets

def hash_with_salt(password: str):
    i = secrets.token_hex(8)
    j = hashlib.sha256(bytes.fromhex(i) + password.encode()).hexdigest()
    return i, j
if __name__ == "__main__":
    x = input("Password: ")
    i, j = hash_with_salt(x)
    print("salt (hex):", i)
    print("hash:", j)
