import os 

nome = input('Digite o nome do aluno: ')
os.system('cls')
nota1 = float(input('Digite a nota da 1° Unidade: '))
os.system('cls')
nota2 = float(input('Digite a nota da 2° Unidade: '))
os.system('cls')
nota3 = float(input('Digite a nota da 3° Unidade: '))
os.system('cls')

media = (nota1+nota2+nota3)/3

if media >=7:
    print(f'{nome} sua média foi: {media:.1f} você foi aprovado')
elif media >=5 and media<7:
    print(f'{nome} sua média foi: {media:.f} você foi para provafinal')
else:
   
    print(f'{nome} sua média foi: {media:.1f} você foi para recuperação')