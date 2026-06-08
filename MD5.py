import struct
import math
 
# Constants for MD5
INIT_A = 0x67452301
INIT_B = 0xefcdab89
INIT_C = 0x98badcfe
INIT_D = 0x10325476
 
# Per-round shift amounts
S = [
    7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,
    5, 9, 14, 20,   5, 9, 14, 20,   5, 9, 14, 20,   5, 9, 14, 20,
    4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,
    6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21
]
 
# Sine-based constants K[i]
K = [int((1 << 32) * abs(math.sin(i + 1))) & 0xFFFFFFFF for i in range(64)]
 
# Left rotate 32-bit integer
def left_rotate(x, amount):
    x &= 0xFFFFFFFF
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF
 
# Padding the message
def md5_padding(message_bytes):
    original_bit_length = (8 * len(message_bytes)) & 0xffffffffffffffff
    message_bytes += b'\x80'  # Append 1 bit (0x80)
    while (len(message_bytes) % 64) != 56:
        message_bytes += b'\x00'  # Pad with zeroes
    message_bytes += struct.pack('<Q', original_bit_length)  # Append length (64-bit LE)
    return message_bytes
 
# Core compression function
def md5_compress(chunk, h0, h1, h2, h3):
    M = list(struct.unpack('<16I', chunk))  # 16 words of 32-bit
 
    A, B, C, D = h0, h1, h2, h3
 
    for i in range(64):
        if 0 <= i <= 15:
            F = (B & C) | (~B & D)
            g = i
        elif 16 <= i <= 31:
            F = (D & B) | (~D & C)
            g = (5 * i + 1) % 16
        elif 32 <= i <= 47:
            F = B ^ C ^ D
            g = (3 * i + 5) % 16
        else:
            F = C ^ (B | ~D)
            g = (7 * i) % 16
 
        F = (F + A + K[i] + M[g]) & 0xFFFFFFFF
        A = D
        D = C
        C = B
        B = (B + left_rotate(F, S[i])) & 0xFFFFFFFF
 
    h0 = (h0 + A) & 0xFFFFFFFF
    h1 = (h1 + B) & 0xFFFFFFFF
    h2 = (h2 + C) & 0xFFFFFFFF
    h3 = (h3 + D) & 0xFFFFFFFF
 
    return h0, h1, h2, h3
 
# Main MD5 function
def md5(message):
    message_bytes = message.encode()
    print('Message Byte: ',message_bytes)
    for i in message_bytes:
        print(i)
    padded = md5_padding(message_bytes)
 
    h0, h1, h2, h3 = INIT_A, INIT_B, INIT_C, INIT_D
 
    for i in range(0, len(padded), 64):
        chunk = padded[i:i + 64]
        h0, h1, h2, h3 = md5_compress(chunk, h0, h1, h2, h3)
 
    # Pack final result into little-endian bytes and convert to hex
    digest = struct.pack('<4I', h0, h1, h2, h3)
    return ''.join(f'{byte:02x}' for byte in digest)
 
# Run the function
if __name__ == "__main__":
    message = input("Enter message to hash using MD5 (from scratch): ")
    hash_value = md5(message)
    print("MD5 Hash:", hash_value)
 