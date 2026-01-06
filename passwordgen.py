import random
import string
def generate_password(length=12):
    """Generate a random secure password"""
    characters =string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("Generated Password:", generate_password(10))


    