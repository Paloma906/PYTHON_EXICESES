import os
import random

secreto = random.randint(1,100)

tentativas = 1

while True:
    palpite = int(input('Digite um número entre 1 e 100: '))
    os.system('cls')
    
    if palpite == secreto:
        print(f'Parabéns você acertou o número secreto em {tentativas} tentativas')
        break
    elif palpite < secreto:
        print('O número secreto é maior!')
        tentativas+=1
    else:
        print('O numero secreto é menor!')
        tentativas+=1
