import time
import json
import requests

def get_unfollowers(username, credentials):
  base_url = "https://api.github.com/" 
  url_followers = str(base_url + "users/" + username + "/following?per_page=100&page=1")

  response_followers = requests.get(url_followers, auth=(username, credentials)).json()

  time.sleep(1)

  for user in response_followers:
    login = json.dumps(user["login"])

    print("GET USER " + login)

    url_follow_back = str(base_url + "/users/" + login + "/following/" + username)
    response_follow_back = requests.get(url_follow_back, auth=(username, credentials))

    print(response_follow_back.status_code)

    time.sleep(1)

    if response_follow_back.status_code == 401:
      url_unfollow = str(base_url + "/" + login)
      requests.delete(url_unfollow, auth=(username, credentials))
      print("UNFOLOW USER " + login + "\n")
      time.sleep(1)
