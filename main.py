import os
import api
from dotenv import load_dotenv

load_dotenv()

GITHUB_SECRET = os.getenv('PERSONAL_ACESS_TOKEN')
USER_NAME = os.getenv('USER')

api.unfollow_back(USER_NAME, GITHUB_SECRET)