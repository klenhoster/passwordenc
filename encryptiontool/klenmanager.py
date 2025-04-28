import tkinter as tk
from cryptography.fernet import Fernet
import pyperclip
import os

# Function to generate a secret key
def generate_key():
    return Fernet.generate_key()

# Function to load or generate a secret key
def load_or_generate_key():
    if os.path.exists("secret.key"):
        with open("secret.key", "rb") as key_file:
            return key_file.read()
    else:
        key = generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        return key

# Encrypt the password
def encrypt_password(password, key):
    fernet = Fernet(key)
    encrypted = fernet.encrypt(password.encode())
    return encrypted

# Decrypt the password
def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted_password).decode()
    return decrypted

# Function to copy to clipboard
def copy_to_clipboard(text):
    pyperclip.copy(text)

# Function to download the encrypted and decrypted passwords as a single text file
def download_passwords(encrypted, decrypted):
    with open("passwords.txt", "w") as file:
        file.write(f"Encrypted Pass:\n{encrypted}\n\nDecrypted Pass:\n{decrypted}")

# GUI
def create_gui():
    key = load_or_generate_key()

    def on_encrypt():
        password = entry_password.get()
        encrypted = encrypt_password(password, key)
        entry_encrypted.delete(0, tk.END)
        entry_encrypted.insert(0, encrypted.decode())

        # Decrypt the password for backup
        decrypted = decrypt_password(encrypted, key)
        entry_decrypted.delete(0, tk.END)
        entry_decrypted.insert(0, decrypted)

    def on_decrypt():
        encrypted = entry_encrypted.get()
        decrypted = decrypt_password(encrypted.encode(), key)
        entry_decrypted.delete(0, tk.END)
        entry_decrypted.insert(0, decrypted)

    def on_copy():
        encrypted = entry_encrypted.get()
        copy_to_clipboard(encrypted)

    def on_download():
        encrypted = entry_encrypted.get()
        decrypted = entry_decrypted.get()
        download_passwords(encrypted, decrypted)

    # Set up the window
    window = tk.Tk()
    window.title("KLEN HOSTER")

    # Password input
    tk.Label(window, text="Enter Password:").grid(row=0, column=0)
    entry_password = tk.Entry(window, show="*")
    entry_password.grid(row=0, column=1)

    # Encrypted password output
    tk.Label(window, text="Encrypted Password:").grid(row=1, column=0)
    entry_encrypted = tk.Entry(window)
    entry_encrypted.grid(row=1, column=1)

    # Decrypted password output
    tk.Label(window, text="Decrypted Password:").grid(row=2, column=0)
    entry_decrypted = tk.Entry(window)
    entry_decrypted.grid(row=2, column=1)

    # Buttons
    button_encrypt = tk.Button(window, text="Encrypt", command=on_encrypt)
    button_encrypt.grid(row=3, column=0)
    
    button_decrypt = tk.Button(window, text="Decrypt", command=on_decrypt)
    button_decrypt.grid(row=3, column=1)

    button_copy = tk.Button(window, text="Copy Encrypted", command=on_copy)
    button_copy.grid(row=4, column=0)

    button_download = tk.Button(window, text="Download Passwords", command=on_download)
    button_download.grid(row=4, column=1)

    # Label to show the creator information
    tk.Label(window, text="Made by klenhoster", font=("Arial", 8), fg="gray").grid(row=5, columnspan=2)

    window.mainloop()

if __name__ == "__main__":
    create_gui()
