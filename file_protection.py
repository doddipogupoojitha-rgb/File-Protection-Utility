#!/usr/bin/env python3
"""
File Protection Utility - AES-256 Encryption
Workora CyberSecurity Task
"""

import os
import argparse
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import secrets

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_file(input_file, password):
    salt = os.urandom(16)
    nonce = os.urandom(12)
    key = derive_key(password, salt)
    
    with open(input_file, 'rb') as f:
        data = f.read()
    
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, data, None)
    
    output_file = input_file + ".enc"
    with open(output_file, 'wb') as f:
        f.write(salt + nonce + ciphertext)
    
    print(f"[+] Encryption Successful!")
    print(f"    Input: {input_file}")
    print(f"    Output: {output_file}")
    return output_file

def decrypt_file(input_file, password):
    with open(input_file, 'rb') as f:
        file_data = f.read()
    
    salt = file_data[:16]
    nonce = file_data[16:28]
    ciphertext = file_data[28:]
    
    key = derive_key(password, salt)
    
    try:
        aesgcm = AESGCM(key)
        plaintext = aesgcm.decrypt(nonce, ciphertext, None)
        
        output_file = input_file.replace(".enc", ".decrypted")
        with open(output_file, 'wb') as f:
            f.write(plaintext)
        
        print(f"[+] Decryption Successful! MAC Verified!")
        return output_file
        
    except Exception as e:
        print(f"[-] Decryption
