import bs4, requests

res = requests.get('https://slickdeals.net/')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

#elems = soup.find_all("div", {"class": "bp-p-dealCard_price"})
#elems = soup.find_all("bp-p-dealCard_price")
elems = soup.find_all(class_="bp-c-card_content")
for elements in elems:
    for link in elements.find_all(class_="bp-c-card_title bp-c-link"):
        print(link.get_text())
    for dealPrice in elements.find_all(class_='bp-p-dealCard_price'):
        print(dealPrice.get_text())
    for originalPrice in elements.find_all(class_='bp-p-dealCard_originalPrice'):
        print(originalPrice.get_text())

#elems = soup.select('#bp244128-DealCard > div > span.bp-p-dealCard_price')
#print(elems)