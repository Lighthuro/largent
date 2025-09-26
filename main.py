from urllib import request, error
from urllib.request import urlopen
from typing import List
from bs4 import BeautifulSoup as bs
from classes import Crypto
import pandas as pd, csv


def main():
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }
    url_site:str="https://coinmarketcap.com/"
    req=request.Request(url=url_site, headers=headers)
    page_cmc = request.urlopen(req).read()
    soup= bs(page_cmc, "html.parser")
    table=soup.find("table", class_="cmc-table")
    table_body=table.find("tbody")
    rows=table_body.find_all("tr")
    cryptos:List[Crypto]=list()
    for row in rows:
        try:
            crypto_name=row.find("p", class_="coin-item-name").text
            crypto_value_div=row.find("div", class_="sc-fa25c04c-0 eAphWs")
            crypto_value:str=crypto_value_div.find("span").text
        except Exception as ex:
            crypto_name=row.contents[2].contents[0].contents[1].contents[0]
            crypto_value:str=row.contents[3].contents[2]

        crypto:Crypto=Crypto(crypto_name=crypto_name, crypto_value=crypto_value)
        cryptos.append(crypto)
    
    with open('database.csv', 'w', newline='\n') as file:
        writer=csv.writer(file)
        writer.writerow(["name","value","timestamp"])
        for crypto in cryptos:
            writer.writerow([crypto.name, crypto.value, crypto.time])
            

if __name__ == '__main__':
    main()