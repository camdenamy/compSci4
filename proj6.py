import random
from math import gcd

# Miller-Rabin primality test
def is_prime(n, k=5):
    if n <= 3:
        return n == 2 or n == 3
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Generate a large prime number
def generate_large_prime(bits=512):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1
        if is_prime(num):
            return num

# Modular inverse
def mod_inverse(e, phi):
    d_old, d = 0, 1
    r_old, r = phi, e
    while r != 0:
        quotient = r_old // r
        d_old, d = d, d_old - quotient * d
        r_old, r = r, r_old - quotient * r
    return d_old % phi

# Generate RSA keys
def generate_keys(bits=512):
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    while p == q:
        q = generate_large_prime(bits)

    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537

    if gcd(e, phi) != 1:
        return generate_keys(bits)

    d = mod_inverse(e, phi)
    return (e, n), (d, n)

# Encrypt
def encrypt(message, pub_key):
    e, n = pub_key
    return [pow(ord(char), e, n) for char in message]

# Decrypt
def decrypt(cipher, priv_key):
    d, n = priv_key
    return ''.join([chr(pow(c, d, n)) for c in cipher])

# Join encrypted numbers into one long string
def format_encrypted(cipher_list):
    return ''.join(str(num) for num in cipher_list)

# Write private key to key.txt
def save_key_to_file(d, n):
    # This will overwrite key.txt if it exists
    with open("key.txt", "w") as f:
        f.write(f"{d}\n")
        f.write(f"{n}\n")

# Main program
if __name__ == "__main__":
    print("Generating RSA key")
    public_key, private_key = generate_keys(bits=512)
    d, n = private_key

    save_key_to_file(d, n)

    message = input("\nEnter the message to laden the swallow: ")
    encrypted = encrypt(message, public_key)
    encrypted_str = format_encrypted(encrypted)
    print("\nEncrypted Message:")
    print(encrypted_str)

    try:
        entered_key = int(input("\nEnter the key to reach the Holy Grail: "))
        if entered_key == d:
            print("\nAccess granted.")
            decrypted = decrypt(encrypted, private_key)
            print("Decrypted Message:", decrypted)
        else:
            print("\nAccess denied. Incorrect key.")
    except ValueError:
        print("\nInvalid input. Must be a number.")
