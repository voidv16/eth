def rc4(key, data):
    """
    Simple RC4 implementation (KSA + PRGA).
    key: bytes or str
    data: bytes or str
    returns: bytes (ciphertext or decrypted plaintext)
    """
    # normalize inputs to bytes
    if isinstance(key, str):
        key = key.encode('utf-8')
    if isinstance(data, str):
        data = data.encode('utf-8')

    # Key-Scheduling Algorithm (KSA)
    S = list(range(256))
    j = 0
    key_len = len(key)
    for i in range(256):
        j = (j + S[i] + key[i % key_len]) & 0xFF
        S[i], S[j] = S[j], S[i]

    # Pseudo-Random Generation Algorithm (PRGA)
    i = 0
    j = 0
    out = bytearray()
    for byte in data:
        i = (i + 1) & 0xFF
        j = (j + S[i]) & 0xFF
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) & 0xFF]
        out.append(byte ^ K)

    return bytes(out)


# Example usage
if __name__ == "__main__":
    plaintext = "MCA Ethical Hacking"
    key = "x"

    ciphertext = rc4(key, plaintext)          # bytes
    print("Ciphertext (hex):", ciphertext.hex())

    decrypted = rc4(key, ciphertext)          # rc4 is symmetric
    print("Decrypted:", decrypted.decode('utf-8'))
