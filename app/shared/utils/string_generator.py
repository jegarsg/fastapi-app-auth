import random
import string

def generate_username(full_name: str) -> str:
    base = ''.join(full_name.lower().split())
    suffix = ''.join(random.choices(string.digits, k=4))
    return f"{base}{suffix}"
