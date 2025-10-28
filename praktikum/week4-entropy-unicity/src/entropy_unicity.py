## Panduan Langkah demi Langkah

import math

# -------------------------------------------
# Langkah 1 — Perhitungan Entropi
# -------------------------------------------
# Rumus: H(K) = log2(|K|)

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("=== Langkah 1: Entropy ===")
print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit\n")


# -------------------------------------------
# Langkah 2 — Menghitung Unicity Distance
# -------------------------------------------
# Rumus: U = H(K) / (R * log2(|A|))
# Keterangan:
# H(K) : Entropi kunci
# R    : Redundansi bahasa (misal: 0.75 untuk Bahasa Inggris)
# |A|  : Ukuran alfabet (contoh: 26 huruf A–Z)

def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
print("=== Langkah 2: Unicity Distance ===")
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK), "karakter\n")


# -------------------------------------------
# Langkah 3 — Analisis Brute Force
# -------------------------------------------
# Simulasi waktu brute force berdasarkan kecepatan komputer tertentu

def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600 * 24)
    return days

print("=== Langkah 3: Analisis Brute Force ===")
print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
