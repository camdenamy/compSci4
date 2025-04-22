import random
from math import gcd

# Miller-Rabin primality test
# Defines a function to check if a number is prime using the Miller-Rabin test. k is the number of rounds for accuracy.
def is_prime(n, k=5):
    # Handles small cases directly. Only 2 and 3 are prime.
    if n <= 3:
        return n == 2 or n == 3
    # Even numbers (except 2) are not prime.
    if n % 2 == 0:
        return False

    # Writes n - 1 = 2 ** r * d, factoring out powers of 2
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Chooses a random base a and computes x = a**d mod n
    for _ in range(k):
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)
        
        # Passes this test round if x is 1 or -1 mod n.
        if x == 1 or x == n - 1:
            continue

        # Repeadtedly squares x and checks if it becomes n - 1; otherwise n is composite
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    # After k tests, the number is most likely prime
    return True

# Generate a large prime number
# Generates a large prime number of specified bit length.
def generate_large_prime(bits=512):
    
    # Generates a random odd number with exactly bits bits.
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1
        # Uses Miller-Rabin to check if it's prime.
        if is_prime(num):
            return num

# Modular inverse
def mod_inverse(e, phi):
    
    # Initialize variables for the extended Euclidean algorithm.
    d_old, d = 0, 1
    r_old, r = phi, e
    
    # Performs the algorithm iteratively.
    while r != 0:
        quotient = r_old // r
        d_old, d = d, d_old - quotient * d
        r_old, r = r, r_old - quotient * r
    
    # Returns modular inverse
    return d_old % phi

# Generate RSA keys
def generate_keys(bits=512):
    
    # Generates two distinct large primes, p and q.
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    while p == q:
        q = generate_large_prime(bits)

    # Computes n = p * q and phi(n), and initilizes public exponent e.
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537

    # ensures e is coprime with phi, else it tries again.
    if gcd(e, phi) != 1:
        return generate_keys(bits)

    # Computes private key d, and returns the public and private key pairs.
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

# Encrypt
# Encrypts each character by turning it into a number and computing c = m**e mod n
def encrypt(message, pub_key):
    e, n = pub_key
    return [pow(ord(char), e, n) for char in message]

# Decrypt
# Decrypts each number with me = c**d mod n, and converts it back to a character
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
# Generates and saves RSA keys
if __name__ == "__main__":
    print("Generating RSA key")
    public_key, private_key = generate_keys(bits=512)
    d, n = private_key

    save_key_to_file(d, n)
    
    # Prompts user for a message, encrypts it, and prints the ciphertext
    message = input("\nEnter the message to laden the swallow: ")
    encrypted = encrypt(message, public_key)
    encrypted_str = format_encrypted(encrypted)
    print("\nEncrypted Message:")
    print(encrypted_str)

    # Asks user to input the private key, and only decrypts the message if it matches the real key.
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
