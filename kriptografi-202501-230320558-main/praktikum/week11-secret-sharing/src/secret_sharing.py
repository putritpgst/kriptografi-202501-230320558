import random

# PRIME besar (jauh lebih besar dari secret string)
PRIME = 2**521 - 1

def polynom(x, coeffs):
    return sum(coef * pow(x, i, PRIME) for i, coef in enumerate(coeffs)) % PRIME

def mod_inverse(a):
    return pow(a, PRIME - 2, PRIME)

def split_secret(secret, threshold, n_shares):
    secret_bytes = secret.encode('utf-8')
    secret_int = int.from_bytes(secret_bytes, 'big')

    if secret_int >= PRIME:
        raise ValueError("Secret terlalu besar untuk PRIME yang dipilih")

    coeffs = [secret_int] + [random.randrange(1, PRIME) for _ in range(threshold - 1)]

    shares = []
    for x in range(1, n_shares + 1):
        y = polynom(x, coeffs)
        shares.append((x, y))
    return shares

def recover_secret(shares):
    secret = 0
    for j, (xj, yj) in enumerate(shares):
        num = 1
        den = 1
        for m, (xm, _) in enumerate(shares):
            if j != m:
                num = (num * (-xm)) % PRIME
                den = (den * (xj - xm)) % PRIME
        lagrange = num * mod_inverse(den)
        secret = (secret + yj * lagrange) % PRIME

    secret_bytes = secret.to_bytes((secret.bit_length() + 7) // 8, 'big')
    return secret_bytes.decode('utf-8')

# =========================
# MAIN
# =========================
secret = "KriptografiUPB2025"

shares = split_secret(secret, 3, 5)

print("Shares:")
for s in shares:
    print(s)

recovered = recover_secret(shares[:3])
print("\nRecovered secret:", recovered)
