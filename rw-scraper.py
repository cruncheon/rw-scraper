# INSTALL PRE-REQS
# sudo apt install tor python3-socks
# sudo service tor start
# pip3 install requests
# pip3 install beautifulsoup4

# RUN
# python3 scrape.py

import requests
from bs4 import BeautifulSoup

# proxy session requests over tor
session = requests.session()
session.proxies["http"] = "socks5h://localhost:9050"
session.proxies["https"] = "socks5h://localhost:9050"

# retrieve "ransomware groups site"
url = "http://ransomwr3tsydeii4q43vazm7wofla5ujdajquitomtd47cxjtfgwyyd.onion"
response = session.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# find and output all the onions to onions.txt
with open("onions.txt", "w") as fs:
    for link in soup.find_all("a"):
        if link.get("href").endswith(".onion"):
            fs.write(link.get("href")+"\n")
