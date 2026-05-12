import hashlib

password = input("Enter a password to hash: ")

# SHA-256 is the industry standard 'fingerprint'
hash_object = hashlib.sha256(password.encode())
hash_hex = hash_object.hexdigest()

print(f"\nPassword: {password}")
print(f"SHA-256 Hash: {hash_hex}")