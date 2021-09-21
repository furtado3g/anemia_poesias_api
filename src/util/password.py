import hashlib

def encrypt_password(password):
    encoded_password = hashlib.sha256(password.encode()).hexdigest()
    return encoded_password