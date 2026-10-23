# File Protection Utility
AES-256 symmetric encryption utility

## Objective
Implement AES-256 symmetric file encryption and PBKDF2 key derivation

## Features
- Uses cryptography library
- PBKDF2 with random salt (16 bytes), 100k iterations
- AES-256-GCM authenticated encryption
- MAC integrity verification
- Encrypts to .enc file

## Usage
pip install cryptography
python file_protection.py encrypt secret.txt mypassword123
python file_protection.py decrypt secret.txt.enc mypassword123
