import requests

r = requests.get("http://google.com/")

# https://www.restapitutorial.com/httpstatuscodes.html  -- HTTP status codes
print("Status:", r.status_code)

print(r.text)

f = open("./page.html", "w+")
f.write(r.text)