import urllib
from bs4 import BeautifulSoup
import pandas as pd


def retrieve_divtable(ticker_symbol):
    data = []
    url = "https://dividata.com/stock/{0}/dividend".format(ticker_symbol.upper())
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    markup = resp.read()
    soup = BeautifulSoup(markup, "lxml")
    table = soup.find_all("table")
    return table
    
def divtable_to_df(resultsetobj):
    data = []
    for row in resultsetobj[0]:
        parse = row.find_all('td')
        if parse:
            newrow = [parse[0].string,parse[1].string]
            data.append(newrow)
    df = pd.DataFrame(data, columns=['ExDivDate', 'DivAmt'])
    return df
    
def get_dividend_history(ticker_symbol):
    data = retrieve_divtable(ticker_symbol)
    df = divtable_to_df(data)
    return df