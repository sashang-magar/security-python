def encrypt(shift:int) -> str:
    plain_text :str = input('\n Enter plain text:')
    cipher_text:str = ''
    for charac in plain_text:
        if charac.isalpha():
            base = ord('A') if charac.isupper() else ord('a')
            cipher_text += chr(((ord(charac) - base + shift) % 26)+ base)
        else:
            cipher_text += charac    
    return cipher_text
    

def decrypt(shift:int) -> str: 
    encrypt_text :str = input('\n Enter decrypt text:')
    plain_text:str = ''
    for charac in encrypt_text:
        if charac.isalpha():
            base = ord('A') if charac.isupper() else ord('a')
            plain_text += chr(((ord(charac) + base - shift) % 26)+ base)
        else:
            plain_text += charac    
    return plain_text 



def main() -> None:
    '''
    Function : entry point of this source code 
    Arguments : none 
    return type : none
    '''
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
            cipher_text = encrypt(shift)
            print(cipher_text)

        else:
            decrypt_text = decrypt(shift)
            print(decrypt_text)
               

if  __name__ == "__main__":
    main()            

           