import customtkinter as ctk        # pra criar a janela/interface
import tkinter
from tkinter import *
from tkinter import messagebox

ctk.set_appearance_mode('dark')

# funcções --------------------------------
def adicionar_tarefa(): 
    tarefa = nova_tarefa.get()
    if tarefa:
        lista_tarefas.insert(0,tarefa)
        nova_tarefa.delete(0,END)
    else: 
        messagebox.showerror('Erro no APP', 'Digite uma tarefa !!')
        
        
def remover_tarefa():
    tarefa_selecionada = lista_tarefas.curselection()
    if tarefa_selecionada:
        lista_tarefas.delete(tarefa_selecionada)
    else:
        messagebox.showerror('Erro no App','Selecione uma tarefa!!')   




#--------------------------------------------

# LISTA DE CORES E FONTES

cor1 = '#00FF7F'
cor2 = '#32CD32'
cor3 = '#DC143C'

font1 = ('Arial', 25, 'bold')
font2 = ('Arial',18,'bold')
font3 = ('Arial',14,'bold')


# -------------------------------------------

janela = ctk.CTk()
janela.geometry('300x480')
janela.title('APP Tarefas V1.0')

ctk.CTkLabel(janela,text='APP Tarefas',font=font1,text_color=cor1).pack(pady=10)

add_tarefas = ctk.CTkButton(janela,text='Adicionar Tarefa',fg_color='blue',width=100,height=30,command=adicionar_tarefa)
add_tarefas.place(x=20,y=80)


remove_tarefas = ctk.CTkButton(janela,text='Remover Tarefa',fg_color='red',width=100,height=30, command=remover_tarefa)
remove_tarefas.place(x= 170,y=80)

nova_tarefa = ctk.CTkEntry(janela,width=250,height=30,placeholder_text='Digite a nova tarefa')
nova_tarefa.pack(pady=100)

ctk.CTkLabel(janela,text='Tarefas Pendentes',font=font2,text_color=cor2).place(x=70,y=200)

lista_tarefas = Listbox(janela, width=40, height= 15)
lista_tarefas.place(x=28,y=230)



janela.mainloop()