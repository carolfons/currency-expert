import customtkinter

#customização de cores
customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

#criando e configurando a janela e outros elementos
janela = customtkinter.CTk() 
janela.geometry("500x500")

#vinculando o elemento com a janela
titulo = customtkinter.CTkLabel(janela, text= "Conversor de Moedas", font=("Times New Roman", 20)) 
lbl_moeda_origem = customtkinter.CTkLabel(janela, text= "Selecione a Moeda de Origem")
lbl_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de Destino")

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=["USD", "BRL","EUR", "BTC"])
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["USD", "BRL","EUR", "BTC"])

def coin_converter():
    print("Converter Moeda")

btn_convert = customtkinter.CTkButton(janela, text="Converter", command=coin_converter)

lista_moedas = customtkinter.CTkScrollableFrame(janela)
moedas_disponiveis = ["USD: Dólar Americano","BRL: Real Brasileiro","EUR: Euro","BTC: Bitcoin"]
for moeda in moedas_disponiveis:
    text_moeda = customtkinter.CTkLabel(lista_moedas, text=moeda)
    text_moeda.pack()

#colocando os elementos na tela
titulo.pack(padx=10, pady=10)
lbl_moeda_origem.pack(padx=10, pady=3)
campo_moeda_origem.pack(padx=10)
lbl_moeda_destino.pack(padx=10,pady=3)
campo_moeda_destino.pack(padx=10)
btn_convert.pack(padx=10,pady=10)
lista_moedas.pack(padx=10, pady=10)


#rodando a janela
janela.mainloop()