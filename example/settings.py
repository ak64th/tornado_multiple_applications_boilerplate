import os
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()

CONFIG_PATH = os.getenv('CONFIG_PATH', '/etc/example/config.py')
DEBUG = os.getenv('DEBUG')

SECRET_KEY = os.getenv('SECRET_KEY')

# DATABASE
DATABASE_URL = os.getenv('DATABASE_URL')
DATABASE_POOL_SIZE = os.getenv('DATABASE_POOL_SIZE', 5)

# JWT
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM', 'HS256')
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', SECRET_KEY)
JWT_AUTH_HEADER_PREFIX = os.getenv('JWT_AUTH_HEADER_PREFIX', 'Bearer')
JWT_LEEWAY = timedelta(seconds=os.getenv('JWT_LEEWAY', 10))
JWT_EXPIRATION_DELTA = timedelta(seconds=os.getenv('JWT_EXPIRATION_DELTA', 300))
JWT_NOT_BEFORE_DELTA = timedelta(seconds=os.getenv('JWT_NOT_BEFORE_DELTA', 0))
JWT_VERIFY_CLAIMS = os.getenv('JWT_VERIFY_CLAIMS', ',').split() or ['signature', 'exp', 'nbf', 'iat']
JWT_REQUIRED_CLAIMS = os.getenv('JWT_REQUIRED_CLAIMS', ',').split() or ['exp', 'nbf', 'iat']
