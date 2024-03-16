import os

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
from dotenv import load_dotenv

load_dotenv()


def get_cipher():
    key_str = os.environ["SECRET_KEY"]
    key = bytes(key_str, "base64")
    algorithm = algorithms.ARC4(key)
    return Cipher(algorithm, mode=None)


def encrypt_info(info: str) -> bytes:
    key_str = os.environ["SECRET_KEY"]
    key = bytes(key_str, "ascii")
    info_bytes = bytes(info, "utf-8")
    return Fernet(key).encrypt(info_bytes)


def decrypt_info(encrypted_info: str) -> str:
    key_str = os.environ["SECRET_KEY"]
    key = bytes(key_str, "ascii")
    info_bytes = bytes(encrypted_info, "ascii")
    return Fernet(key).decrypt(info_bytes).decode("utf-8")
