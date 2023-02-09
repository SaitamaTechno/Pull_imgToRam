from bs4 import BeautifulSoup
import requests

def get_sources(keyword):
    url = "https://www.google.com/search?q=" + str(keyword) + "&source=lnms&tbm=isch"
    HEADERS = {"content-type": "image/png"}
    html = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(html, "html.parser")
    mylist=[]
    for img in soup.find_all("img"):
        mylist.append(img["src"])
    return mylist
