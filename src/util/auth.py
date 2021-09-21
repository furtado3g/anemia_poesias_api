import jwt
from src.util.password import encrypt_password
def create_token(payload, secret):
    token = jwt.encode(payload=payload,algorithm='HS256',key=secret,)
    return token
