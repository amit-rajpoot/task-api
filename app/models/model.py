from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base


"""<-------USER------->"""
class User(Base):
    __tablename__ = "users"
    id =Column(Integer, primary_key = True, index = True)
    email =Column(String , unique = True , nullable = False , index = True)
    hashed_password =Column(String,nullable=False)
    is_active =Column(Boolean, default=True)
    tasks = relationship("Task" , back_populates="owner")

"""<-------TASKS------->"""
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    priority = Column(String, nullable=True, default="LOW")
    due_date = Column(DateTime, nullable=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(
        DateTime,
        default=datetime.utcnow)
    owner = relationship("User", back_populates="tasks")