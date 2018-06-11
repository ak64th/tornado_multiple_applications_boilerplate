from sqlalchemy import Column, Integer, String
from tornado_sqlalchemy import declarative_base
from werkzeug.security import check_password_hash, generate_password_hash

Base = declarative_base()


class App(Base):
    __tablename__ = 'app'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    info = Column(String(100), nullable=False)
    key = Column(String(100), nullable=False)
    secret = Column(String(100), nullable=False)
    status = Column(Integer, nullable=False)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    status = Column(Integer, nullable=False)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_password(self, password):
        self.password = generate_password_hash(password)
