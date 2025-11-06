from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
public_key = key.publickey()

encrypt_cipher = PKCS1_OAEP.new(public_key)
decrypt_cipher = PKCS1_OAEP.new(key)

message = input("Enter message to encrypt: ").encode()

encrypted_message = encrypt_cipher.encrypt(message)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt_cipher.decrypt(encrypted_message)
print("Decrypted Message:", decrypted_message.decode())
