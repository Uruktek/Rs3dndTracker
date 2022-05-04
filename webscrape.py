import time
import requests
from bs4 import BeautifulSoup

class_ = "table-bg-grey"  # TODO: Add green to check as well.
sites = ["https://runescape.wiki/w/Sinkholes",
         "https://runescape.wiki/w/Big_Chinchompa"]

while True:
    for site in sites:
        responseFromSites = requests.get(url=site)
        time.sleep(5)  # Sleep is 100% needed do not remove.
        # grabbing the http content from the site
        soupSinkholes = BeautifulSoup(responseFromSites.content, 'html.parser')
        # TODO: Make this work for either grey and green
        tableValueSinkholes = soupSinkholes.find("td", class_)
        # This block extracts the number of mins from the site.
        minsFromSite = []
        for word in tableValueSinkholes.string.split():
            if word.isdigit():
                minsFromSite.append(int(word))
        print(minsFromSite)
