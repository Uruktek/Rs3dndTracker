import requests
from bs4 import BeautifulSoup

class_ = "table-bg-grey"  # TODO: Add green to check as well.
#urlForSinkHoles = "https: // runescape.wiki/w/Sinkholes"
#urlForBigChin = "https://runescape.wiki/w/Big_Chinchompa"

# getting the link from the site
# TODO: Make this work for more than one url
# FIXME: url can't accept a var for some reason?
responseFromSinkholes = requests.get(
    url="https://runescape.wiki/w/Sinkholes",
)
# print(response.status_code)

# grabbing the htlp content from the site
soupSinkholes = BeautifulSoup(responseFromSinkholes.content, 'html.parser')

# looking for table-bg-grey or green

# TODO: Make this work for either grey and green
tableValueSinkholes = soupSinkholes.find("td", class_)
print(tableValueSinkholes.string)
