# password_manager
Secure CLI password manager with encryption, storage, updates, and suggestions. Data saved in JSON, passwords encrypted using Fernet for protection.


# 🔐 Encrypted Password Manager

A secure, command-line password manager built with Python. It allows users to store, retrieve, update, and delete account credentials, generate strong passwords, and persist data across sessions using encrypted storage.

## 🚀 Features

- Store and retrieve account credentials
- Update usernames and passwords
- Delete accounts securely
- Generate strong random passwords
- Encrypt passwords using Fernet symmetric encryption
- Persist data in a local JSON file
- Smooth text display for enhanced CLI experience

## 🛠 Requirements

- Python 3.6+
- `cryptography` library

Install dependencies:
```bash
pip install cryptography
```

## 🔧 Setup

1. Generate an encryption key:
   ```python
   from cryptography.fernet import Fernet
   print(Fernet.generate_key())
   ```
2. Replace `key = b'your_saved_key_here'` in the script with your generated key.
3. Run the script:
   ```bash
   python password_manager.py
   ```

## 📁 Data Storage

- Credentials are saved in `credentials.json`
- Passwords are encrypted before being stored

## ⚠️ Disclaimer

This tool is for educational use. Do not use it to store sensitive data without proper security practices.


