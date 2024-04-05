from bs4 import BeautifulSoup as bs4
import random
import re as regex
import requests
import os
import sys

from urllib.parse import urlparse

OUTPUT_DIR = sys.argv[1]
START_AT = int(sys.argv[2])
ALBUM_URL = sys.argv[3]
USER_AGENTS = [
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/108.0.5359.71 Safari/537.36", 
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
]
HEADERS = {'User-Agent': random.choice(USER_AGENTS)}

def download(url:str):
  if not (os.path.exists(OUTPUT_DIR)):
    os.makedirs(OUTPUT_DIR)
  fileName = os.path.join(OUTPUT_DIR, os.path.basename( urlparse( url ).path ))
  response = requests.get(url, headers=HEADERS, stream=True)
  print(response.headers)
  with open(fileName, mode="wb") as file:
    for chunk in response.iter_content(1024):
      file.write(chunk)

page = requests.get(ALBUM_URL)
soup = bs4(page.content, "html.parser")
grid = soup.find("div", {"class", "grid-images"})

media = regex.findall(r"<a.+?href=\"(.+?)\".*?>", str( grid ))
for index in range(START_AT, len(media)):
  print("Downloading entry {}/{}".format(index+1, len(media)))
  if (regex.search(r"/i/", media[index])):
    print("Image ", media[index])

    page = requests.get(media[index])
    soup = bs4(page.content, "html.parser")
    _media = str( soup.find_all("a")[-2] )
    _link = regex.findall(r"<a.+?href=\"(.+?)\".*?>", _media)[0]
    
    print(_link)
    download(_link)

  if (regex.search(r"/v/", media[index])):
    print("Video ", media[index])

    page = requests.get(media[index])
    soup = bs4(page.content, "html.parser")
    _media = str( soup.find("a", {"id": "czmDownloadz"}) )
    _link = regex.findall(r"<a.+?href=\"(.+?)\".*?>", _media)[0]
    
    page = requests.get(_link)
    url = regex.findall(r"<a.+?href=\"(.+?)\".*?>", page.text)[0]
    
    print(url)
    download(url)