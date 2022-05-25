import requests
from pprint import pprint

site = "https://api.jikan.moe/v4/anime?q="
user_input = input("Enter Anime Name: ").lower()

req = requests.get("https://api.jikan.moe/v4/anime?q=" + user_input)


# pprint(req.content, indent=2)
# pprint(req.text)
# print(req.__dict__["_content"])

x = req.json()
data = x["data"]
d_data = data[0]


title = d_data["title"]
status = d_data["status"]
description = d_data["synopsis"]
aired = d_data["aired"]
start = aired["from"] 
end = aired["to"]
print(type(start), type(end))
episodes = d_data["episodes"]

print(f"""
Title: {title}
Status: {status}


Summary: {description}

Date Aired: {start} - {end}
Episodes: {episodes}
""")