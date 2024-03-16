from datetime import datetime, timedelta

from personal_streamlit.models.key_info import KeyInfo
from personal_streamlit.tools.encryption import decrypt_info, encrypt_info


def is_valid_key(key: str) -> bool:
    info = decrypt_info(key)
    key_info = KeyInfo.model_validate_json(info)
    return key_info.expiration > datetime.now()


def create_key():
    expiration_date = datetime.now() + timedelta(days=1)
    info = KeyInfo(expiration=expiration_date)
    info_json = info.model_dump_json()
    return encrypt_info(info_json).decode()
