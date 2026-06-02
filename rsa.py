# RSA Algorithm in Python

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def find_d(e, phi):
    d = 1
    while (d * e) % phi != 1:
        d += 1
    return d


# Key Generation
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

n = p * q
phi = (p - 1) * (q - 1)

e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 1

d = find_d(e, phi)

print("\nPublic Key (e, n):", (e, n))
print("Private Key (d, n):", (d, n))

# Encryption
message = int(input("\nEnter message (integer less than n): "))

cipher = pow(message, e, n)
print("Encrypted Message:", cipher)

# Decryption
decrypted = pow(cipher, d, n)
print("Decrypted Message:", decrypted)