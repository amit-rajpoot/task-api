from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

# DATABASE URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db"

# ENGINE
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread":False
    }
)

# Session
SessionLocal = sessionmaker(autoflush=False,
                            autocommit=False,
                            bind=engine)

# BASE
Base = declarative_base(
    
)

# Function for Database 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()