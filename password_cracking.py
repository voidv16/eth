import hashlib

# Simulating a password hash (let's assume the correct password is 'password123')
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


# Dictionary attack: try each password from the dictionary and compare its hash
def dictionary_attack(hash_to_crack: str, dictionary: list) -> str | None:
    for password in dictionary:
        # Hash each password in the dictionary and compare it to the given hash
        hashed = hash_password(password)
        if hashed == hash_to_crack:
            return password  # Password found
    return None  # Password not found


if __name__ == "__main__":
    # Test the function
    original_password = "password123"
    hashed_password = hash_password(original_password)

    # Simulating a dictionary attack
    dictionary = ["admin", "password", "123456", "letmein", "password123"]
    found_password = dictionary_attack(hashed_password, dictionary)

    if found_password:
        print(f"Password found: {found_password}")
    else:
        print("Password not found in dictionary.")
