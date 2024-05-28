import customtkinter as ctk

from tkinter import *

# calcular
def calcular():
    valor1 = float(receita1.get())
    valor2 = float(receita2.get())
    valor3 = float(despesa1.get())
    valor4 = float(despesa2.get())
    valor5 = float(despesa3.get())
    valor6 = float(despesa4.get())

    saldoFinal = (valor1 + valor2 ) - (valor3 + valor4 + valor5 + valor6)

    resultado.configure(text = f'Seu saldo final foi: R$ {saldoFinal:.2f}');


ctk.set_appearance_mode('Dark')
janela = ctk.CTk()

janela = ctk.CTk()
janela.geometry('550x800')


ctk.CTkLabel(janela,text="Controle de gastos", font=('ARIAL', 20, 'bold')).pack(pady = 20)



receita1 = ctk.CTkEntry(janela, placeholder_text="Digite a sua primeira receita", width=350, height=60, font=("arial", 15, "bold"))
receita1.pack(pady = 10)

receita2 = ctk.CTkEntry(janela, placeholder_text="Digite a sua segunda receita", width=350, height=60, font=("arial", 15, "bold"))
receita2.pack(pady = 10)

despesa1 = ctk.CTkEntry(janela, placeholder_text="Digite a sua primeira despesa", width=350, height=60, font=("arial", 15, "bold"))
despesa1.pack(pady = 10)

despesa2 = ctk.CTkEntry(janela, placeholder_text="Digite a sua segunda despesa", width=350, height=60, font=("arial", 15, "bold"))
despesa2.pack(pady = 10)

despesa3 = ctk.CTkEntry(janela, placeholder_text="Digite a sua terceira despesa", width=350, height=60, font=("arial", 15, "bold"))
despesa3.pack(pady = 10)

despesa4 = ctk.CTkEntry(janela, placeholder_text="Digite a sua quarta despesa", width=350, height=60, font=("arial", 15, "bold"))
despesa4.pack(pady = 10)

botao = ctk.CTkButton(janela, text="Calcular", width=120, height=50, command=calcular)
botao.pack(pady=10)







resultado = ctk.CTkLabel(janela, font=('Arial', 20, "bold") , text=" ")
resultado.pack(pady=20)


janela.mainloop()











