import time
import requests
from bs4 import BeautifulSoup

tableColors = ["table-bg-grey", "table-bg-green"]
# For loop over the two options it can be and check for errors?
# the only alt is to have an if the class_ doesn't return one to check the other.
sites = ["https://runescape.wiki/w/Sinkholes",
         "https://runescape.wiki/w/Big_Chinchompa"]

while True:
    for site in sites:
        for tableColor in tableColors:
            responseFromSites = requests.get(url=site)
            time.sleep(1)  # Sleep is 100% needed do not remove.

            # grabbing the http content from the site
            soupSinkholes = BeautifulSoup(
                responseFromSites.content, 'html.parser')

            tableValueSinkholes = soupSinkholes.find("td", tableColor)

            # print(type(tableValueSinkholes))
            if tableValueSinkholes is None:
                print('beep')
            # FIXME: RESOLVE THE LOOP SO THIS CAN ACTUALL WORK

            # # This block extracts the number of mins from the site.
            # minsFromSite = []
            # for word in tableValueSinkholes.string.split():
            #     if word.isdigit():
            #         minsFromSite.append(int(word))
            # print(minsFromSite)
