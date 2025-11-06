import string

def xor_cipher(data, key):
    result = []
    data_bytes = data.encode('utf-8')
    key_bytes = key.encode('utf-8')
    key_len = len(key_bytes)

    for i in range(len(data_bytes)):
        xored_byte = data_bytes[i] ^ key_bytes[i % key_len]
        result.append(chr(xored_byte))

    return "".join(result)


PLAINTEXT = "MCA Ethical Hacking"
SECRET_KEY = "x"
CIPHERTEXT = xor_cipher(PLAINTEXT, SECRET_KEY)

print(f"Original Plaintext: {PLAINTEXT}")
print(f"Secret Key Used: '{SECRET_KEY}'")
# show a bytes representation so unprintable characters are visible
print(
    "Generated Ciphertext (may contain unprintable chars):",
    repr(CIPHERTEXT.encode('utf-8'))
)
print("-" * 50)

print("Starting Brute-Force Attack...")
POSSIBLE_KEYS = string.ascii_lowercase
FOUND = False

for attempt_key in POSSIBLE_KEYS:
    decrypted_text = xor_cipher(CIPHERTEXT, attempt_key)
    # exact comparison to the original plaintext
    if decrypted_text == PLAINTEXT:
        print("\nDecryption Successful!")
        print(f"Key Found: '{attempt_key}'")
        print(f"Plaintext: {decrypted_text}")
        FOUND = True
        break

if not FOUND:
    print("Brute-force failed to find a key matching the expected plaintext.")
