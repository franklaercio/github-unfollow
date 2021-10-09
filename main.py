from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Chrome(executable_path=r'/home/frank/workspace/python/github-unfollow/chomerdriver')
driver.get("http://www.python.org")
assert "Python" in driver.title