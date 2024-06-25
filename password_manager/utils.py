from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
from cryptography.fernet import Fernet, InvalidToken
import json
import base64
import os
import string
import secrets


def derive_key(password: str, salt: bytes) -> bytes:
    kdf = Scrypt(
        salt=salt,
        length=32,
        n=2**14,
        r=8,
        p=1,
        backend=default_backend()
    )
    
    key = kdf.derive(password.encode())
    
    return base64.urlsafe_b64encode(key)


def load_encrypted_json_data(filename: str, password: str) -> dict:
    try:
        with open(filename, 'rb') as file:
            encrypted_data = file.read()
        
        salt = encrypted_data[:16]
        encrypted_data = encrypted_data[16:]
        
        key = derive_key(password, salt)
        
        fernet = Fernet(key)
        
        decrypted_data = fernet.decrypt(encrypted_data).decode()
        
        return json.loads(decrypted_data)
    
    except FileNotFoundError:
        return {}
    
    except InvalidToken:
        raise ValueError('Invalid master password provided')
    
    except Exception as e:
        raise RuntimeError('Failed to decrypt data') from e
    
    
def save_encrypted_json_data(filename: str, data: dict, password: str) -> None:
    salt = os.urandom(16)
    key = derive_key(password, salt)
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(json.dumps(data).encode())
    
    fd = os.open(filename, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    
    with os.fdopen(fd, 'wb') as file:
        file.write(salt)
        file.write(encrypted_data)


def credentials_already_exist(website_data: dict, website: str, username: str) -> bool:
    return any(username == data['username'] for data in website_data[website])


def find_index_by_key_value(lst: list, key: str, value: str) -> int:
    return next((i for i, d in enumerate(lst) if d.get(key) == value), -1)


def generate_password(length: int, use_special_chars: bool = False) -> str:
    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password