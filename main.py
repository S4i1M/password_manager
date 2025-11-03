import time
import sys
import random
import json
import os
from cryptography.fernet import Fernet

key = b'your_saved_key_here'
cipher = Fernet(key)

def encrypt_password(password):
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()

def smooth_flow(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

DATA_FILE = "credentials.json"

def load_credentials():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {}

def save_credentials():
    with open(DATA_FILE, "w") as file:
        json.dump(passwords, file)

passwords = load_credentials()

numbers_string = '0123456789'
lowercase_string = 'abcdefghijklmnopqrstuvwxyz'
uppercase_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_symbols_string = "!@#$%^&*()-_+=[]\\{}|;:',.<>/?`~"

numbers_list = list(numbers_string)
lowercase_list = list(lowercase_string)
uppercase_list = list(uppercase_string)
special_symbols_list = list(special_symbols_string)

def generate_password(length=12):
    all_chars = numbers_list + lowercase_list + uppercase_list + special_symbols_list
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def suggest_passwords(num_suggestions=3, length=12):
    suggestions = []
    for _ in range(num_suggestions):
        suggestions.append(generate_password(length))
    return suggestions

def store_credentials(account_name, username, password):
    encrypted = encrypt_password(password)
    passwords[account_name] = {
        "user_name": username,
        "user_password": encrypted
    }
    save_credentials()
    smooth_flow(f"Credentials for {account_name} stored.", delay=0.02)

def retrieve_credentials(account_name):
    if account_name in passwords:
        smooth_flow(f"Account: {account_name}", delay=0.02)
        smooth_flow(f"Username: {passwords[account_name]['user_name']}", delay=0.02)
        decrypted = decrypt_password(passwords[account_name]['user_password'])
        smooth_flow(f"Password: {decrypted}", delay=0.02)
    else:
        smooth_flow(f"Account {account_name} not found.", delay=0.02)

def change_username(account_name, new_username):
    if account_name in passwords:
        passwords[account_name]["user_name"] = new_username
        save_credentials()
        smooth_flow(f"Username for {account_name} changed to {new_username}.", delay=0.02)
    else:
        smooth_flow(f"Account {account_name} not found.", delay=0.02)

def change_password(account_name, new_password):
    if account_name in passwords:
        encrypted = encrypt_password(new_password)
        passwords[account_name]["user_password"] = encrypted
        save_credentials()
        smooth_flow(f"Password for {account_name} changed.", delay=0.02)
    else:
        smooth_flow(f"Account {account_name} not found.", delay=0.02)

def delete_account(account_name):
    if account_name in passwords:
        del passwords[account_name]
        save_credentials()
        smooth_flow(f"Account {account_name} deleted.", delay=0.02)
    else:
        smooth_flow(f"Account {account_name} not found.", delay=0.02)

while True:
    try:
        options = ("1. Store password\n2. Change password\n3. Change username\n4. Show password\n5. Suggest Password\n6. Delete account\n7. Exit")
        smooth_flow(options, delay=0.02)
        user_input = int(input("Enter your option: "))

        if user_input == 1:
            account = input("Enter account name: ")
            user = input("Enter username: ")
            password = input("Enter password: ")
            store_credentials(account, user, password)

        elif user_input == 2:
            account = input("Enter account name: ")
            new_password = input("Enter new password: ")
            change_password(account, new_password)

        elif user_input == 3:
            account = input("Enter account name: ")
            new_user = input("Enter new username: ")
            change_username(account, new_user)

        elif user_input == 4:
            account = input("Enter account name: ")
            retrieve_credentials(account)

        elif user_input == 5:
            suggestions = suggest_passwords()
            smooth_flow("Password Suggestions:", delay=0.02)
            for suggestion in suggestions:
                smooth_flow(suggestion, delay=0.02)

        elif user_input == 6:
            account = input("Enter account name to delete: ")
            delete_account(account)

        elif user_input == 7:
            smooth_flow("Exiting...", delay=0.02)
            break
        else:
            smooth_flow("Invalid option.", delay=0.02)

    except ValueError:
        smooth_flow("Invalid input. Please enter a number.", delay=0.02)


Let me know if you'd like to add a master password or a login system next.
