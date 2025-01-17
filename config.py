from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
BASE_URL = os.getenv("BASE_URL")
VALID_USERNAME = os.getenv("VALID_USERNAME")
VALID_PASSWORD = os.getenv("VALID_PASSWORD")
INVALID_USERNAME = os.getenv("INVALID_USERNAME")
INVALID_PASSWORD = os.getenv("INVALID_PASSWORD")