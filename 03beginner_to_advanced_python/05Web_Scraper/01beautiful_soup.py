from bs4 import BeautifulSoup
import requests

# When you get data from the internet is called web scraping

search = input("Enter Search Term: ")
params = {"q": search}
r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
print(soup.prettify())
