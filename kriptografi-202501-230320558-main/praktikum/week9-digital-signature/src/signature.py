from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# --- Variabel Global ---
KEY_SIZE = 2048
MESSAGE = b"Hello, ini pesan penting."
MODIFIED_MESSAGE = b"Hello, ini pesan palsu."

def generate_keys():
    """Menghasilkan pasangan kunci RSA (2048-bit)."""
    # print("🔑 1. Menghasilkan pasangan kunci RSA...")
    key = RSA.generate(KEY_SIZE)
    private_key = key
    public_key = key.publickey()
    print("    Kunci berhasil dibuat.")
    return private_key, public_key

def sign_message(private_key, message):
    """Membuat tanda tangan digital menggunakan kunci privat."""
    print("\n✍️ 2. Membuat Tanda Tangan Digital...")
    # 1. Hitung hash dari pesan
    h = SHA256.new(message)
    print(f"    Hash Pesan Asli (SHA256): {h.hexdigest()[:16]}...")

    # 2. Tanda tangani hash menggunakan skema PKCS#1 v1.5
    signer = pkcs1_15.new(private_key)
    signature = signer.sign(h)
    print("    Tanda Tangan berhasil dibuat.")
    print(f"    Signature (Hex): {signature.hex()[:32]}...")
    return signature, h

def verify_signature(public_key, hash_object, signature, description):
    """Memverifikasi tanda tangan menggunakan kunci publik."""
    print(f"\n✅/❌ 3. Verifikasi Tanda Tangan ({description})...")
    
    # Kunci publik digunakan untuk verifikasi
    verifier = pkcs1_15.new(public_key)

    try:
        # Coba verifikasi. Jika gagal, akan memicu ValueError atau TypeError
        verifier.verify(hash_object, signature)
        print("    Verifikasi berhasil: Tanda tangan valid.")
    except (ValueError, TypeError):
        print("    Verifikasi GAGAL: Tanda tangan tidak cocok dengan pesan atau kunci.")

# =================================================================
#                         EKSEKUSI PROGRAM
# =================================================================

# Langkah 1: Generate Key
private_key, public_key = generate_keys()

# Langkah 2: Buat Tanda Tangan
signature, original_hash = sign_message(private_key, MESSAGE)

# Langkah 3: Verifikasi Tanda Tangan (Kasus Berhasil)
# Menggunakan hash asli (original_hash)
verify_signature(public_key, original_hash, signature, "Kasus Berhasil (Pesan dan Tanda Tangan Asli)")


# Langkah 4: Uji Integritas (Kasus Gagal karena pesan diubah)
print("\n--- UJI MODIFIKASI PESAN ---")
# 1. Hitung hash dari pesan palsu
fake_hash = SHA256.new(MODIFIED_MESSAGE)
print(f"    Hash Pesan Palsu (SHA256): {fake_hash.hexdigest()[:16]}...")

# 2. Coba verifikasi signature ASLI dengan hash PESAN PALSU
verify_signature(public_key, fake_hash, signature, "Kasus Gagal (Pesan Dimodifikasi)")