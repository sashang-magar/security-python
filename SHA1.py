import struct

# Left rotate function
def left_rotate(n, b):
    return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF


# SHA-1 implementation
def sha1(message):

    # Convert message to bytes
    message = message.encode()

    # Original length in bits
    original_length = len(message) * 8

    # Append '1' bit
    message += b'\x80'

    # Pad with zeros until length becomes 448 mod 512
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'

    # Append original length (64-bit big-endian)
    message += struct.pack(">Q", original_length)

    # Initialize hash values
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    # Process each 512-bit block
    for i in range(0, len(message), 64):

        chunk = message[i:i + 64]

        # Break into sixteen 32-bit words
        w = list(struct.unpack(">16I", chunk))

        # Extend to 80 words
        for j in range(16, 80):
            temp = w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16]
            w.append(left_rotate(temp, 1))

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        # 80 rounds
        for j in range(80):

            if j <= 19:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999

            elif j <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1

            elif j <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC

            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (
                left_rotate(a, 5)
                + f
                + e
                + k
                + w[j]
            ) & 0xFFFFFFFF

            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        # Update hash values
        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    # Return final hash
    return "%08x%08x%08x%08x%08x" % (h0, h1, h2, h3, h4)


# Main program
message = input("Enter message: ")
print("SHA-1 Hash:", sha1(message))