from cryptography.fernet import Fernet

# pip install cryptography
# Generate a key for encryption/decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypting the password
password = "mysecretpassword"
encrypted_password = cipher_suite.encrypt(password.encode())

# Decrypting the password
decrypted_password = cipher_suite.decrypt(encrypted_password).decode()

# Display results
print("Original Password:", password)
print("\n\nEncrypted Password:", encrypted_password)
print("\n\nDecrypted Password:", decrypted_password)
