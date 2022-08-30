from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()

def gen_key():
        with open('filekey.key', 'wb') as filekey:
            filekey.write(key)

def load_key():
    with open('filekey.key', 'rb') as fkey:
        key = fkey.read()

def encrypt_file():
        f = Fernet(key)
        filename = input("Enter file to encrypt: ")
        with open(filename, "rb") as file:
            context = file.read()
            encrypted = f.encrypt(context)
            with open('encrypted_file.txt', 'wb') as file:
                file.write(encrypted)

def decrypt_file():
    f = Fernet(key)
    file_name = input("Enter file to decrypt: ")
    with open(file_name, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
        decrypted = f.decrypt(encrypted)
        with open('decrypted_file.txt', 'wb') as file:
            file.write(decrypted)


def check_key_load():
    print(key)


def main():
    print("(1) generate a key     (2) Encrypt file    (3) Check key    (4) Decrypt File   (5) Load key  (q) Quit")
    choice = input("Enter choice: ")
    if choice == "1":
        gen_key()
        os.system("cls")
        main()
        
    elif choice == "2":
        encrypt_file()
        os.system("cls")
        main()

    elif choice == "3":
        check_key_load()
        os.system("cls")
        main()
    elif choice == "4":
        decrypt_file()
        os.system("cls")
        main()
    elif choice == "5":
        load_key()
        print("Key Loaded")
        os.system("cls")
        main()
    elif choice == "q":
        exit()
    else:
        print("doesnt exist")

main()
