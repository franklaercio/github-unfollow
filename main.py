import os
import api
from dotenv import load_dotenv

load_dotenv()

def main():
  GITHUB_SECRET = os.getenv('PERSONAL_ACESS_TOKEN')
  USER_NAME = os.getenv('USER')
  BASE_URL = os.getenv('BASE_URL')
  TIME_SLEEP = os.getenv('TIME_SLEEP')

  api.unfollow_back(BASE_URL, TIME_SLEEP, USER_NAME, GITHUB_SECRET)

if __name__ == "__main__":
    main()