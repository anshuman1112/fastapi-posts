from passlib.context import CryptContext

#Password Encryption
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_hash(password: str):
    return pwd_context.hash(password)

def verify(plain_pwd, hashed_pwd):
    return pwd_context.verify(plain_pwd, hashed_pwd)
