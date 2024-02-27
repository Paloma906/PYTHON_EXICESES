#for x in range(30):
    #print('Paloma')
    
#pessoas = ['Paloma','Isadora','Lucas Barauna','Emannoel','Léo']


#total = len(pessoas)

#for x in range(total):
 #   if pessoas[x].startswith('L'):
 #       print(pessoas[x])
 
 
    
#for x in pessoas:
#    if x.startswith('L'):
#        print(x)

# -----------------------------------------------------------------------------------------------------------------------------------
#Exercicio 1: Escreva um programa que conta quantos números positivos e quantos números negativos existem em uma lista de números.

#Separe em vetores e imprima somente os positivos e somente os negativos

#Definindo a lista de números
#numeros = [5,-3,10,8,-2,15,7,-9,4,6]

#numero = [5,-3,10,8,-2,15,7,-9,4,6]

#positivo_count = []
#negativo_count = []

#for x in numero:
    
    #if(x>=0):
#        positivo_count.append(x)
    #else:
#        negativo_count.append(x)
        
#print(f'NUMEROS POSITIVOS:  {positivo_count}')
#print(f'NUMEROS NEGATIVOS:  {negativo_count}')
#print(f'Total de números positivos é:  {len(positivo_count)}')
#print(f'Total de números negativos é:  {len(negativo_count)}')

#------------------------------------------------------------------------------------------------------------------------------------------

#Exercicio 2: Imprima os números ímpares, imprima o somatório do vetor, imprima a média do vetor

valores = [22,33,44,23,26,29,67,56,45,46,32,11,17]

num_impar = []
num_par =[]

for x in valores:
    
    if (x % 2 == 0):
        num_par.append(x)
    else:
        num_impar.append(x)
        
media = sum(valores)/len(valores)
        
print(f'Numeros pares: {num_par}')
print(f'Numeros ímpares: {num_impar}')
print(f'Somatorio dos valores: {sum(valores)}')
print(f'Média do vetor: {media:.2f}')


#-----------------------------------------------------------------------------------------------------------------
    
    