import json
import re
from urllib import response
import requests
from pprint import pprint
from backend.app.database.user import deactivate_by_id

from backend.tools.update_user import SAMPLE_USER

URL = "http://127.0.0.1:5000/users/"

SAMPLE_USER = {
    "first_name": "Anthony",
    "last_name": "Fauxci",
    "hobbies": "Experimenting"
}

def get_user():
    user_id = input("Type in desired user id:")
    url = "%s%s" % (URL, user_id)
    response = requests.get(url)
    user = {}
    if response.status_code == 200:
        response_json = response.json()
        user = response_json["user"][0]
        print("User: ")
        pprint(user)
    else:
        print("Errors while trying to retrieve user")
    return user.get("id")

def deactivate_user(user_id):
    url = "%s%s" % (URL, user_id)
    response = requests.delete(url)
    if response.status_code == 204:
        print("User deactivated")
    else:
        print("Error while trying to deactivate user")
    
if __name__ == "__main__":
    print("DEACTVATE USER")
    user_id = get_user()
    deactivate_by_id(user_id)

    

