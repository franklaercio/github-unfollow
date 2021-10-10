import time
import json
import requests

def get_unfollowers(username, credentials, page_number):
  base_url = "https://api.github.com/" 
  url_followers = str(base_url + "users/" + username + "/following?per_page=1&page=" + str(page_number))

  response_followers = requests.get(url_followers, auth=(username, credentials)).json()

  time.sleep(2)

  for user in response_followers:
    login = json.dumps(user["login"]).replace("\"", "").replace("\"", "")
    url_follow_back = base_url + "users/" + login + "/following/" + username
    response_follow_back = requests.get(url_follow_back, auth=(username, credentials))

    time.sleep(1)

    if response_follow_back.status_code == 404:
      url_unfollow = base_url + "user/following/" + login

      response_unfollow = requests.delete(url_unfollow, auth=(username, credentials))

      if response_unfollow.status_code == 204:
        print("Unfollowing " + login + "!")
      else:
        print("Could not unfollow " + login + "!")

      time.sleep(1)

  return len(response_followers) < 100 

def unfollow_back(username, credentials):
  next_page = True
  page_number = 1

  while next_page:
    has_next_page = get_unfollowers(username, credentials, page_number)

    if has_next_page:
      page_number += 1
    else:
      next_page = False