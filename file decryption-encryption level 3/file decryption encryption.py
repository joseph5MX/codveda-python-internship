from cryptography.fernet import Fernet
import os

KEY_FILENAME = "secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILENAME, "wb") as key_file:
        key_file.write(key)
    print(f"New key generated and saved to {KEY_FILENAME}")

def load_key():
    if not os.path.exists(KEY_FILENAME):
        print("No key found. Generating one now...")
        generate_key()
    with open(KEY_FILENAME, "rb") as key_file:
        return key_file.read()

def encrypt_file(filename, key):
    fernet = Fernet(key)
    try:
        with open(filename, "rb") as f:
            data = f.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return

    encrypted_data = fernet.encrypt(data)
    new_filename = filename + ".encrypted"
    with open(new_filename, "wb") as f:
        f.write(encrypted_data)
    print(f"File encrypted and saved as {new_filename}")

def decrypt_file(filename, key):
    fernet = Fernet(key)
    try:
        with open(filename, "rb") as f:
            data = f.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return

    try:
        decrypted_data = fernet.decrypt(data)
    except Exception:
        print("Error: Decryption failed. Wrong key or corrupted file.")
        return

    new_filename = filename.replace(".encrypted", ".decrypted")
    with open(new_filename, "wb") as f:
        f.write(decrypted_data)
    print(f"File decrypted and saved as {new_filename}")

def main():
    key = load_key()

    while True:
        print("\n--- File Encryption Tool ---")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            filename = input("Enter filename to encrypt: ")
            encrypt_file(filename, key)
        elif choice == "2":
            filename = input("Enter filename to decrypt: ")
            decrypt_file(filename, key)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()