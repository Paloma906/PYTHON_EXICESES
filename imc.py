import os

nome=input('Digite o seu nome: ')
os.system('cls')
peso=float(input('Digite o seu peso: '))
os.system('cls')
altura=float(input('Digite a sua altura: '))
os.system('cls')

imc = peso/(altura*altura)

if (imc < 18.5 ):
    print(f'{nome} está abaixo do peso')
elif (imc >=18.5 and imc < 25):
    print(f'{nome} está com o peso normal')
elif (imc >=25 and imc <29.9):
    print(f'{nome} está com sobrepeso')
else:
    print(f'{nome} está pré-obeso')

