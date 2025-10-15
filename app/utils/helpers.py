# app/utils/helpers.py
import hashlib
import uuid

def generate_uuid() -> str:
    return str(uuid.uuid4())

def hash_string(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()
