import requests


r = requests.get("https://ihned.cz")
print(r.status_code)
