import customtkinter
from search_currency import currency_name, available_exchange


#customização de cores
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

#criando e configurando a janela e outros elementos
janela = customtkinter.CTk() 
janela.geometry("500x500")

dic_conversoes_disp = available_exchange()

#vinculando o elemento com a janela
titulo = customtkinter.CTkLabel(janela, text= "Conversor de Moedas", font=("Times New Roman", 25)) 
lbl_moeda_origem = customtkinter.CTkLabel(janela, text= "Selecione a Moeda de Origem")
lbl_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de Destino")

#função para mostrar as moedas disponíveis depois que escolher a moeda inicial
def load_exchange(selected_exchange):
    exchange_list = dic_conversoes_disp[selected_exchange]
    campo_moeda_destino.configure(values=exchange_list)
    campo_moeda_destino.set(exchange_list[0])

#a função do botão manda como parâmetro qual opção selecionada
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disp.keys()), command= load_exchange) #pega as chaves dicionario e transforma em lista
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["Selecione uma moeda de origem"])

def coin_converter():
    print("Converter Moeda")

btn_convert = customtkinter.CTkButton(janela, text="Converter", command=coin_converter)

lista_moedas = customtkinter.CTkScrollableFrame(janela)
available_currency = currency_name()

for codigo_moeda in available_currency:
    currency_name = available_currency[codigo_moeda]
    text_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {currency_name}")
    text_moeda.pack()

#colocando os elementos na tela
titulo.pack(padx=10, pady=10)
lbl_moeda_origem.pack(padx=10, pady=3)
campo_moeda_origem.pack(padx=10)
lbl_moeda_destino.pack(padx=10,pady=3)
campo_moeda_destino.pack(padx=10)
btn_convert.pack(padx=10,pady=20)
lista_moedas.pack(padx=10, pady=10)


#rodando a janela
janela.mainloop()