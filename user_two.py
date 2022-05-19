from sqlalchemy import Column, String, Integer, VARCHAR, TIMESTAMP
from base import Base


class UserTwo(Base):

    __tablename__ = "user_two"
    user_two_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username_two = Column(VARCHAR(16))
    email_two = Column(String(256), nullable=False)
    password_two = Column(VARCHAR(32), nullable=False)
    create_time_two = Column(TIMESTAMP)

    def __init__(self, email: str, password: str, username: str = None):
        self.email_two = email
        self.password_two = password
        self.username_two = username
        