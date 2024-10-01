import xmltodict

def currency_name():
    with open("moedas.xml","rb") as arquivo_moedas: #abre o arquivo no formato de apenas leitura
        dict_moedas = xmltodict.parse(arquivo_moedas)
        moedas = dict_moedas["xml"]
        return moedas
    

def available_exchange():
    with open("available.xml","rb") as arquivo_conversoes: #abre o arquivo no formato de apenas leitura
        dict_conversoes = xmltodict.parse(arquivo_conversoes)
        
    exchange = dict_conversoes["xml"]
    dict_conversoes_disponiveis = {}
    
    #percorre o dicionário preenchendo um outro dicionário
    for couple_exchange in exchange:
        exchange_start, exchange_end = couple_exchange.split("-") #separa em moeda inicial e moeda que pode ter câmbio
        
        #{"USD":["BRL","CAD","AUD"]}
        if exchange_start in dict_conversoes_disponiveis:
            dict_conversoes_disponiveis[exchange_start].append(exchange_end)
        else:
            dict_conversoes_disponiveis[exchange_start] = [exchange_end]
    

    return dict_conversoes_disponiveis

