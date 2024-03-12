import customtkinter as ctk

janela = ctk.CTk('darkred')
janela.minsize(500,500)
janela.maxsize(600,500)
janela.title('Teça de Login')


titulo = ctk.CTkLabel(janela,text='Tela de Login',font=('arial',30,'bold'),text_color='white')
titulo.pack(pady=20)

login = ctk.CTkEntry(janela,placeholder_text='Digite o seu Login', width=350,height=50,fg_color='darkgray',text_color='darkred') 
login.pack(pady=10)

senha = ctk.CTkEntry(janela,placeholder_text='Digite a sua senha', width=350,height=50,show='•') #pra pôr a bolinha é alt 7
senha.pack(pady=10)

lembrar = ctk.CTkCheckBox(janela,text='Lembrar Login',text_color='white')
lembrar.pack()

botao = ctk.CTkButton(janela,text='Login',fg_color='white',text_color='red')
botao.pack(pady=20)
   


janela.mainloop()