import os
from dotenv import load_dotenv


load_dotenv()
S3_BUCKET = os.getenv("S3_BUCKET")
S3_KEY = os.getenv("S3_KEY")
S3_SECRET = os.getenv("S3_SECRET")
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")
