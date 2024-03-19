import customtkinter as ctk

#funções -----------------------------------

def formula():
    n1 =float(nota1.get())
    n2 =float(nota2.get())
    n3 =float(nota3.get())
    
    media = (n1+n2+n3)/3
    
    if (media >= 7):
        resultado.configure(text=f'Sua Média foi {media:.1f}, \n você foi aprovado!')
    else:
        resultado.configure(text=f'Sua Média foi {media:.1f}, \n você foi para a recuperação!')
        
def limpar():
    nota1.delete(0,'end')
    nota2.delete(0,'end')
    nota3.delete(0,'end')
    resultado.configure(text='')
    
        




#-------------------------------------------

ctk.set_appearance_mode('dark')

janela = ctk.CTk()
janela.minsize(600,400)
janela.title('Sistema Escolar V1.0')

ctk.CTkLabel(janela,text='Sistema Escolar versão 1.0',font=('Arial',27,'bold'),text_color='green').pack(pady=5)

nota1 = ctk.CTkEntry(janela,placeholder_text='Digite a nota da 1º Unidade',width=400,height=30)
nota1.pack(pady=20)

nota2 = ctk.CTkEntry(janela,placeholder_text='Digite a nota da 2º Unidade',width=400,height=30)
nota2.pack(pady=20)

nota3 = ctk.CTkEntry(janela,placeholder_text='Digite a nota da 3º Unidade',width=400,height=30)
nota3.pack(pady=20)

botao = ctk.CTkButton(janela,text='Calcular',fg_color='green',text_color='white',width=100,height=30,cursor='star',command=formula)
botao.pack(pady=10)

botao_limpar = ctk.CTkButton(janela,text='Limpar',fg_color='darkred',text_color='white',width=100,height=30,cursor='star',command=limpar)
botao_limpar.pack(pady=10)



resultado = ctk.CTkLabel(janela,text='',font=('Arial',20,'bold'),text_color='white')
resultado.pack(pady=5)




janela.mainloop()