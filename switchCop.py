import requests
from bs4 import BeautifulSoup

URL = 'https://seattle.craigslist.org/search/sss?query=nintendo+switch&sort=date&search_distance=5.2&postal=98008'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

postCode = input("Enter your Postal Code: ")
distance = input("Enter the max distance you're willing to travel: ")

if not(postCode == ''):
    URL = URL.replace('98008', str(postCode))
if not(distance == ''):
    URL = URL.replace('5.2', str(distance))

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

price = soup.findAll("span", {"class": "result-price"})


finalPrices = []
finalItems = []
counter = 0
for hit in soup.findAll(attrs={'class' : 'result-title'}):
    finalItems.append(hit.contents[0].strip())

for obj in price:
    counter+=1
    if (counter%2 == 0):
        finalPrices.append(str(obj).strip("<span class=\"result-price\">").strip("</"))

print("\nThe prices for your query currently are: \n")
for i in range(len(finalItems)):
    print(finalPrices[i] + " - " + finalItems[i], end='\n')
