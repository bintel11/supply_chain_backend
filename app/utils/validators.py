# app/utils/validators.py
import re
from pydantic import validator

def validate_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_password(password: str) -> bool:
    # Minimum 8 chars, at least one letter and one number
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
    return re.match(pattern, password) is not None
