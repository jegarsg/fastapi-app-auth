# app/modules/user/utils/username_helper.py
import random
import string

def generate_username(full_name: str) -> str:
    base = ''.join(full_name.lower().split())
    suffix = f"{random.randint(10,99)}{''.join(random.choices(string.ascii_lowercase, k=3))}"
    return base + suffix
