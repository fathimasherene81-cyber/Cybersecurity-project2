import hashlib

# This represents a 'stolen' hash from a database
target_hash = "fd120da47c525c975f526e94d0fa481ff55be8b18e3829a9b894191652497928" # This is the hash for 'password'

# A small list of common passwords to try
common_passwords = ["123456", "admin", "hello", "password","Banana77", "qwerty"]

print("--- Starting Brute Force Attack ---")

for guess in common_passwords:
    # Hash the guess
    guess_hash = hashlib.sha256(guess.encode()).hexdigest()
    
    print(f"Trying: {guess} -> {guess_hash}")
    
    if guess_hash == target_hash:
        print(f"\n[!] MATCH FOUND! The password is: {guess}")
        break
else:
    print("\n[-] Password not found in list.")