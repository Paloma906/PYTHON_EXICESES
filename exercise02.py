
import os

nome = input('Digite o seu nome: ')
os.system('clear')

peso = float(input('Digite o seu peso: '))
os.system('clear')

altura = float(input('Digite a sua altura: '))
os.system('clear')

imc = peso/(altura*altura)

print(f'Sr(a) {nome} o seu imc é {imc:.2f}')