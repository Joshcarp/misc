# Add users from stdio to github repo, Used for adding users to go course 
#
#
﻿from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from getpass import getpass

driver = webdriver.Chrome()
driver.get("https://github.com/login")
github_username = input("enter your Github username\n")
github_password = getpass("enter password\n")
url = input("Please enter the git URL eg. https://github.com/joshcarp/misc")

password = driver.find_element_by_xpath("//*[@id=\"password\"]")
username = driver.find_element_by_xpath("//*[@id=\"login_field\"]")

username.send_keys(github_username)
password.send_keys(github_password)

time.sleep(1)

driver.find_element_by_xpath("//*[@id=\"login\"]/form/div[3]/input[4]").click()
driver.get(f"{url}/settings/collaboration")


time.sleep(1)


added_already = 0

non_added = []
time.sleep(1)
print("tab enter to escape")

while True:
    time.sleep(1)
    add_user_box = driver.find_element_by_xpath("//*[@id=\"search-member\"]")
    confirm_box = driver.find_element_by_xpath("//*[@id=\"collaborators\"]/form/div[1]/div/div[2]/span/button")

    user = input("enter username to add to repo\n")
    if user == "\t":
        break
    add_user_box.clear()
    time.sleep(1)
    add_user_box.send_keys(user)
    time.sleep(2)
    try:
        top_result = driver.find_element_by_xpath("//*[@id=\"repo-collab-complete-results-option-0\"]")
        if "isn’t a GitHub member" in top_result.text:
            non_added.append(user)
            print("error adding user: No result\n")
            continue
        if user.lower() != top_result.text.lower().split()[0]:
            non_added.append(user)
            continue
    except:
        non_added.append(user)
        print("error adding user:", user, " No result\n")
        continue

    try:
        top_result.click()
        time.sleep(1)
        confirm_box.click()
    except:
        pass
    try:
        time.sleep(1)
        already_added = driver.find_element_by_xpath("//*[@id=\"collaborators\"]/form/div[2]")
        if "User is already" in already_added.text or "User has already" in already_added.text:
            added_already += 1

    except:
        pass

print("already_added =", added_already)

print("Error adding following users:")
for user in non_added:
    print(user)
