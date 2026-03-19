def encrypt():
    plain_text = input('\n Enter the plain text:')
    key_text = input('\n Enter the key text:')
    encrypt_text = ''
    key_index = 0
    for char in plain_text: 
        if char.isalpha():
            p = ord(char) -97
            k = ord(key_text[key_index % len(key_text)]) - 97

            new_text = (p+k) % 26
            encrypt_text += chr(new_text +97)
            key_index +=1
        
        else:
            encrypt_text += char

        print("Encrypted text:", encrypt_text)

def main() -> None :
    while True:
        print('\n 1. Encrypt')
        print('\n 1. Decrypt')
        print('\n 1. Exit')

        choice = input('Enter a option:')

        if choice == '1':
            encrypt()
        if choice == '2':
            pass
        if choice == '3':
            break
