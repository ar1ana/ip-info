import time
import json
import requests

target_ip = input("targets ip:")
api = "http://ip-api.com/json/"

res = requests.get(api + target_ip)

data = res.json()

print("IP Country Is: ", data["lat"])
# print("The IP You Are Tracking Is: ", target_ip)
