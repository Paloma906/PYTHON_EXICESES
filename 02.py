import os


nome = input('Digite o seu nome: ')

os.system('shutdown /s') 

os.system('clear')

# os.system('shutdown /s') 

valor01 = float(input('Digite o primeiro numero: '))  #input armazena o valor como string, precisa converter.
os.system('clear')

valor02 = float(input('Digite o segundo numero: '))
os.system('clear')

calculo = valor01*valor02

print(f'{nome} a multiplicação dos dois números foi: {calculo}')





