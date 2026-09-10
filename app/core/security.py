from datetime import datetime , timedelta
from typing import Union
from jose import JOSEError , jwt
from app.core.config import pwd_context , ACCESS_TOKEN_EXPIRE_MINUTES , SECRET_KEY ,ALGORITHM

def get_password_hash(password:str) -> str:
    """Hash password using Argon2(NO length limit,Secure)"""
    return pwd_context.hash(password)

def verify_password(plain_password:str , hashed_password:str)->bool:
    """Verify password by Argon2"""
    return pwd_context.verify(plain_password,hashed_password)

def create_access_token(data:dict , expires_delta:Union[timedelta,None]=None):

    to_encode = data.copy()

    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))

    to_encode.update({"exp":expire})

    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)