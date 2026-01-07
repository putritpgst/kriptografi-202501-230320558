# --- Aritmetika Modular ---
def mod_add(a, b, n):
    return (a + b) % n

def mod_sub(a, b, n):
    return (a - b) % n

def mod_mul(a, b, n):
    return (a * b) % n

def mod_exp(base, exp, n):
    return pow(base, exp, n)

# --- GCD & Extended Euclidean ---
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n

# --- Logaritma Diskrit (brute-force, untuk contoh kecil) ---
def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

# --- Main: jalankan semua uji satu kali ---
def main():
    print("=== Langkah 1: Aritmetika Modular ===")
    print("7 + 5 mod 12 =", mod_add(7, 5, 12))
    print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
    print("7^128 mod 13 =", mod_exp(7, 128, 13))
    print()

    print("=== Langkah 2: GCD (Euclidean Algorithm) ===")
    print("gcd(54, 24) =", gcd(54, 24))
    print()

    print("=== Langkah 3: Extended Euclidean & Invers Modular ===")
    print("Invers 3 mod 11 =", modinv(3, 11))
    print()

    print("=== Langkah 4: Logaritma Diskrit ===")
    print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))
    print()

if __name__ == "__main__":
    main()
