import requests
import io

params = {"q": "pizza"}
r = requests.get("http://www.bing.com/search", params=params)
print("Status:", r.status_code)

print(r.url)

f = open("./page.html", "w+", encoding="utf-8")
f.write(r.text)
