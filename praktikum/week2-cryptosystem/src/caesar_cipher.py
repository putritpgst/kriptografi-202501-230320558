def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

# Input dari pengguna
msg = input("Masukkan teks yang ingin dienkripsi: ")
key = int(input("Masukkan kunci (angka): "))

# Enkripsi
enc = caesar_encrypt(msg, key)
# Dekripsi
dec = caesar_decrypt(enc, key)

# Output
print("\n=== HASIL ===")
print("Plaintext  :", msg)
print("Ciphertext :", enc)
print("Decrypted  :", dec)
