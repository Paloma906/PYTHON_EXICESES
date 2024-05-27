import customtkinter as ctk        # pra criar a janela/interface
import tkinter
from tkinter import *
from tkinter import messagebox

def calcular():
    carga = float(cargaHoraria.get())
    qdtFaltas = int(faltas.get())
    total_aulas = carga/4
    faltas_permitidas = (total_aulas * 25)
    porcentagem_faltas = (qdtFaltas/total_aulas) * 100
    faltas_restantes = faltas_permitidas - qdtFaltas

    if (qdtFaltas > faltas_permitidas):
         resultado.configure(text=f'Você ultrapassou a quantidade de faltas permitidas!')
    else:
         resultado.configure(text=f'Você tem {porcentagem_faltas} de faltas , você ainda pode faltar {faltas_restantes}')




#/-------------------------------------------------------------------------------

ctk.set_appearance_mode('white')

janela = ctk.CTk('#434343') 
janela.geometry('500x600')
janela.title('Tela de Acesso')

titulo = ctk.CTkLabel(janela,text='Quantos dias posso faltar?',font=('arial',30,'bold'),text_color='white')
titulo.pack(pady=20)

cargaHoraria = ctk.CTkEntry(janela,placeholder_text='Digite a carga horaria da matéria', width=350,height=50,fg_color='white',text_color='black') 
cargaHoraria.pack(pady=10)

faltas = ctk.CTkEntry(janela,placeholder_text='Digite a quantidade de dias que faltou', width=350,height=50,fg_color='white',text_color='black') 
faltas.pack(pady=10)

botao = ctk.CTkButton(janela,text='Calcular',fg_color='white',text_color='black', command=calcular)
botao.pack(pady=20)


#funções






   
    


resultado = ctk.CTkLabel(janela,text='',font=('Arial',20,'bold'),text_color='black')
resultado.pack(pady=5)


janela.mainloop()