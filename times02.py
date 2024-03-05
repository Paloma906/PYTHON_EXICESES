import os


times= [
    "Boyern de Munique",
    "Borussia Dortmund",
    "Leipzig",
    "Barcelona",
    "Real Madrid",
    "Atlético de Madrid",
    "Real Sociedad",
    "Manchester City",
    "Arsenal",
    "Inter de Milão",
    "Napoli",
    "Psg",
    "Porto",
    "Copenhague",
    "PSV",
    "Lazio"
    
]

print('Bem vindo ao Jogo da Adivinhação!')
print('Tente advinhar - 3 times da Champions League!')

def jogo(times):
    
    pontos = 0
    
    for x in range(3):
        palpite = input('Digite um time: ').capitalize().strip()
        
        if palpite in times:
            pontos+=1
            os.system('cls')
            print(f'Parabéns você acertou {pontos} time(s), você tem {pontos} pontos !')
            times.remove(palpite)
            
            
        else:
            os.system('cls')
            print(f'Este time não está na lista, você tem {pontos} pontos!')
            
            
            
jogo(times)
        
        