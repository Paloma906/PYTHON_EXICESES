import customtkinter as ctk
import os

#funções ----------------

def desligar():
    os.sytem('shutdown /s /t 0')

def reiniciar():
    os.sytem('shutdown /r /t 0')
    
def bloquear():
    os.sytem('shutdown /l /t 0')
#-----------------------------------

janela=ctk.CTk('black')
janela.minsize(300,500)
janela.title('Bomba Patch ')

ctk.CTkLabel(janela,text='Bomba Patch V1.0',font=('arial',30,'bold'),text_color='whitesmoke').pack(pady=10)

bt01 = ctk.CTkButton(janela,text='Desligar',font=('arial',30,'bold'),fg_color='white',text_color='black',command=desligar)
bt01.pack(10)

bt02 = ctk.CTkButton(janela,text='Reiniciar',font=('arial',30,'bold'),fg_color='white',text_color='black',command=reiniciar)
bt02.pack(pady=10)

bt03 = ctk.CTkButton(janela,text='Bloquear',font=('arial',30,'bold'),fg_color='white',text_color='black',command=bloquear)
bt03.pack()




# shutdown comandos // pesquisar no google

janela.mainloop()