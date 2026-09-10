from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
import os


SECRET_KEY = os.getenv("SECRET_KEY","change_this_secret_for_prod")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60*24*7 #7days 24hour 60minute

pwd_context = CryptContext(schemes=['argon2'],deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "/auth/token")