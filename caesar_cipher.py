def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

message = input("Enter a message to encrypt: ")
shift_value = int(input("Enter shift value (1-25): "))

encrypted_message = encrypt(message, shift_value)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, shift_value)
print("Decrypted Message:", decrypted_message)
