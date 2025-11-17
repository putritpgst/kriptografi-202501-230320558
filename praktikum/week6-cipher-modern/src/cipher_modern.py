# ================================ #
#             DES Cipher           #
# ================================ #
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Kunci 64 bit (8 byte)
key = get_random_bytes(8)
cipher = DES.new(key, DES.MODE_ECB)

# Plaintext harus 8 byte (kelipatan 8)
plaintext = b"ABCDEFGH"
ciphertext = cipher.encrypt(plaintext)

print("=== DES ===")
print("Ciphertext:", ciphertext)

# Dekripsi
decipher = DES.new(key, DES.MODE_ECB)
decrypted = decipher.decrypt(ciphertext)

print("Decrypted :", decrypted)
print()


# ================================ #
#             AES Cipher           #
# ================================ #
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)  # 128-bit key
cipher = AES.new(key, AES.MODE_EAX)

plaintext = b"Modern Cipher AES Example"

ciphertext, tag = cipher.encrypt_and_digest(plaintext)

print("=== AES ===")
print("Ciphertext:", ciphertext)

# Dekripsi
cipher_dec = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
decrypted = cipher_dec.decrypt(ciphertext)

print("Decrypted :", decrypted.decode())
print()


# ================================ #
#              RSA Cipher          #
# ================================ #
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate key pair
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Enkripsi menggunakan public key
cipher_rsa = PKCS1_OAEP.new(public_key)
plaintext = b"RSA Example"
ciphertext = cipher_rsa.encrypt(plaintext)

print("=== RSA ===")
print("Ciphertext:", ciphertext)

# Dekripsi menggunakan private key
decipher_rsa = PKCS1_OAEP.new(private_key)
decrypted = decipher_rsa.decrypt(ciphertext)

print("Decrypted :", decrypted.decode())
