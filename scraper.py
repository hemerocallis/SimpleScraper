from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    try:
        html = urlopen("http://en.wikipedia.org" + articleUrl)
    except HTTPError as e:
        print(e.code)
        return None
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        linksList = bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    except AttributeError as e:
        print("Attribute cannot be found")
        return None
    return linksList

links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
