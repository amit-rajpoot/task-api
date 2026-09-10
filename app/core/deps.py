from fastapi import Depends , HTTPException , status
from sqlalchemy.orm import Session
from jose import JWTError , jwt
from app.db.database import  get_db 
from app.core.config import SECRET_KEY , ALGORITHM , oauth2_scheme
from app.models.model import User

def get_current_user(
        token:str = Depends(oauth2_scheme),
        db:Session = Depends(get_db)
):
    credentials_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not Validate Authentication token",
        headers= {"WWW-Authencate":"bearer"},
    )
    try:
        payload = jwt.decode(token,
                             SECRET_KEY,
                             algorithms=[ALGORITHM])
        user_id:str = payload.get("sub")
        if user_id is None:
            raise credentials_error
    except JWTError:
        raise credentials_error
    
    user = db.query(User).filter(User.id == int(user_id)).first()
    if user is None:
            raise credentials_error
    return user

