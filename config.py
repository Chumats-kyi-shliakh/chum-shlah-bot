import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
USE_REDIS = os.getenv('USE_REDIS')
