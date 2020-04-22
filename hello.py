import requests


r = requests.get("https://denikn.cz")
print(r.status_code)
