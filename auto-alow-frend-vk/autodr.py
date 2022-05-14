import time
import requests
import json


def main():
    while True:
        with open("config.json", "r") as f:
            data = json.loads(f.read())
            for token in data["tokens"]:
                my_id = requests.get(f"https://api.vk.com/method/account.getProfileInfo?access_token={token}&v=5.131").json()["response"]["id"]
                subs = requests.get(
                    f"https://api.vk.com/method/users.getFollowers?user_id={my_id}&access_token={token}&v=5.131").json()["response"]["items"]
                if len(subs) != 0:
                    for sub in subs:
                        r = requests.get(
                            f"https://api.vk.com/method/friends.add?user_id={sub}&access_token={token}&v=5.131").json()
                        print(r)
                        time.sleep(10)
        with open("config.json", "r") as f:
            data = json.loads(f.read())
        time.sleep(int(data["timesleep"]))


if __name__ == '__main__':
    main()
