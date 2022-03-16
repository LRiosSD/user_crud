
import requests
from pprint import pprint

URL = "Http:/127.0.0.1:500/users/"

SAMPLE_USER = {
    "first_name": "Anthony",
    "last_name": "Fauci",
    "hobbies": "Experimenting"
}
def update_user(user_id):
    SAMPLE_USER["first_name"] = input("Enter a first name:")
    SAMPLE_USER["last_name"] = input("Enter a last name:")
    SAMPLE_USER["hobbies"] = input("Enter hobbies:")
    url = "%s%s" % (URL, user_id)
    response = requests.put(url, jason=SAMPLE_USER)
    if response.status_code == 204:
        print("User updated.")
    else:
        print("Error while trying tupdate user.")

def get_user():
    user_id = input("Type in the desired user id:")
    url = "%s%d" % (URL, user_id)
    response = requests.get(url)
    user = {}
    if response.status_code==200:
        response_json = response.json()
        user = response_json["users"][0]
        print("User: ")
        pprint(user)
    else:
        print("Error while trying to retrieve user.")
    return user.get("id")
        

if __name__ == "__main__":
    print("UPDATE USER")
    print("---------")
    user_id = get_user()
    update_user(user_id)
