import secrets
import os
from dotenv import load_dotenv

load_dotenv()

# Database URI with a more secure fallback
SQLALCHEMY_DATABASE_URI = os.environ.get(
    "SQLALCHEMY_DATABASE_URI",
    "sqlite:///task_management.sqlite"  # Using the same fallback as in render.yaml
)

# Disable SQLAlchemy track modifications to improve performance
SQLALCHEMY_TRACK_MODIFICATIONS = False

# JWT secret key, read from the environment (never commit it)
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or secrets.token_urlsafe(48)  # set JWT_SECRET_KEY in production
