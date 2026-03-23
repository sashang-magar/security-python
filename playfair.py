def generate_matrix(key):
    key = key.lower().replace('j', 'i')
    matrix = []
    used = set()

    for char in key:
        if char.isalpha() and char not in used:
            matrix.append(char)
            used.add(char)

    for char in "abcdefghiklmnopqrstuvwxyz":
        if char not in used:
            matrix.append(char)

    return [matrix[i:i+5] for i in range(0, 25, 5)]


def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j


def prepare_text(text):
    text = text.lower().replace('j', 'i')
    prepared = ""
    i = 0

    while i < len(text):
        a = text[i]
        if i + 1 < len(text):
            b = text[i+1]
        else:
            b = 'x'

        if a == b:
            prepared += a + 'x'
            i += 1
        else:
            prepared += a + b
            i += 2

    if len(prepared) % 2 != 0:
        prepared += 'x'

    return prepared


def encrypt_playfair():
    key = input("\nEnter key: ")
    text = input("Enter plaintext: ")

    matrix = generate_matrix(key)
    text = prepare_text(text)

    print("\n5x5 Matrix:")
    for row in matrix:
        print(" ".join(row))

    cipher = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]

        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            cipher += matrix[row1][(col1 + 1) % 5]
            cipher += matrix[row2][(col2 + 1) % 5]

        elif col1 == col2:
            cipher += matrix[(row1 + 1) % 5][col1]
            cipher += matrix[(row2 + 1) % 5][col2]

        else:
            cipher += matrix[row1][col2]
            cipher += matrix[row2][col1]

    print("\nEncrypted text:", cipher)


def main():
    while True:
        print("\n--- Playfair Cipher ---")
        print("1. Encrypt")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            encrypt_playfair()
        elif choice == '2':
            break
        else:
            print("Invalid choice")


main()