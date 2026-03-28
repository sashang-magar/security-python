def encrypt_rail_fence(text: str, key: int) -> str:
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]

    direction_down = False
    row, col = 0, 0

    # Fill zig-zag
    for char in text:
        if row == 0 or row == key - 1:
            direction_down = not direction_down

        rail[row][col] = char
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    # Read row-wise
    cipher_text = ""
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                cipher_text += rail[i][j]

    return cipher_text
def decrypt_rail_fence(text: str, key: int) -> str:
    # create empty matrix
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]

    # mark zig-zag pattern
    direction_down = None
    row, col = 0, 0

    for i in range(len(text)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        rail[row][col] = '*'
        col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    # fill matrix row-wise with ciphertext
    index = 0
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] == '*' and index < len(text):
                rail[i][j] = text[index]
                index += 1

    # now read zig-zag to get original text
    result = ""
    row, col = 0, 0
    direction_down = None

    for i in range(len(text)):
        if row == 0:
            direction_down = True
        if row == key - 1:
            direction_down = False

        if rail[row][col] != '\n':
            result += rail[row][col]
            col += 1

        if direction_down:
            row += 1
        else:
            row -= 1

    return result

def main():
    while True:
        print("\n--- Rail Fence Cipher ---")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            plain_text = input("Enter the plaintext: ")
            key = int(input("Enter the key (number of rails): "))

            result = encrypt_rail_fence(plain_text, key)
            print("Encrypted text:", result)

        elif choice == '2':
            cipher_text = input("Enter the ciphertext: ")
            key = int(input("Enter the key (number of rails): "))

            result = decrypt_rail_fence(cipher_text, key)
            print("Decrypted text:", result)


        elif choice == '3':
            break
        else:
            print("Invalid choice")


main()