def encrypt(shift:int) -> str:
    plain_text :str = input('\n Enter plain text:')
    cipher_text:str = ''

def main() -> None:
    while True:
        print("\n Select Options:")
        print("\n 1. Encrypt")
        print("\n 2. Decrypt")
        print("\n 3. Exit")

        choice : str = input("\n Enter your opinion ").strip()

        if choice == '3':
            print('\n Existing the program..bye ')
            break
        if choice not in {'1' , '2'}:
            print ('\n Invalid Options')
            continue
        shift :int =int(input('\n Enter the value of shift:'))

        if choice == '1':
            encrypt()