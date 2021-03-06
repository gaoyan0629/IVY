# from urllib.request import urlopen
from urllib import urlopen
from bs4 import BeautifulSoup

def get_currency_rates(base="USD"):
    """ The file at location url is read in and the exchange rates are extracted """
    url = "https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote"
    data = urlopen(url).read()
    data = data.decode('utf-8')
    soup = BeautifulSoup(data, 'html.parser')
    data = soup.get_text()
    print data

    flag = False
    currencies = {}
    for line in data.splitlines():
        if flag:
            value = float(line)
            flag = False
            currencies[currency] = value
        if line.startswith("USD/"):
            flag = True
            currency = line[4:7]
    
    currencies["USD"] =  1 # we must add it, because it's not included in file
    if base != "USD":
        base_currency_rate = currencies[base] 
        for currency in currencies:
            currencies[currency] /= base_currency_rate

    return currencies
