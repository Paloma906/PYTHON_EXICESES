numeros=[10,20,30,40,50]

def media(numeros):
    
    quantidade=len(numeros)
    somatorio=sum(numeros)
    resultado= somatorio/quantidade
    return resultado

def imprimir():
    
    valorFinal = media(numeros)
    
    print(f'A média do vetor é {valorFinal}')
    
    
imprimir()