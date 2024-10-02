import requests


def convert_currency(currency_start,currency_end):
    
    link=f"https://economia.awesomeapi.com.br/last/{currency_start}-{currency_end}"
    response = requests.get(link)

    bid = response.json()[f"{currency_start}{currency_end}"]["bid"] #pega o valor do "bid": no json resposta
    return bid