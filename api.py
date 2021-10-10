import time
import json
import requests

def find_users_per_page(base_url, time_sleep, username, credentials, page_number):
  url = str(base_url + "users/" + username + "/following?per_page=100&page=" + str(page_number))
  response = requests.get(url=url, auth=(username, credentials)).json()

  time.sleep(int(time_sleep))

  if response != 403:
    return response
  else: 
    print("Check your number connections or followings!")
    return  

def find_unfollowers(base_url, time_sleep, username, credentials, list_users, list_unfollows):
  for user in list_users:
    login = json.dumps(user["login"]).replace("\"", "").replace("\"", "")
    url = base_url + "users/" + login + "/following/" + username

    response = requests.get(url, auth=(username, credentials))

    time.sleep(int(time_sleep))

    if response.status_code == 404:
      list_unfollows.append(login)
      print("User " + login + " doesn't follow you!")
    elif response.status_code == 403:
      print("You exceeded the maximum number of connections!")
      return False   
    else:
      print("User " + login + " follow you!")    

  return len(list_users) == 100 

def delete_user(base_url, time_sleep, username, credentials, list_unfollows):
    for login in list_unfollows:
      response = requests.delete(str(base_url + "user/following/" + login), 
          auth=(username, credentials))

      if response.status_code == 204:
        print("Unfollowing " + login + "!")
      elif response.status_code == 403:
        print("You exceeded the maximum number of connections!")
        break  
      else:
        print("Could not unfollow " + login + "!")
        
      time.sleep(int(time_sleep))

def unfollow_back(base_url, time_sleep, username, credentials):
  list_unfollows = []
  next_page = True
  page_number = 1

  while next_page:
    list_users = find_users_per_page(base_url, time_sleep, username, credentials, page_number)

    there_is_next_page = find_unfollowers(base_url, time_sleep, username, 
        credentials, list_users, list_unfollows)

    if there_is_next_page:
      page_number += 1
    else:
      next_page = False

  delete_user(base_url, time_sleep, username, credentials, list_unfollows)    