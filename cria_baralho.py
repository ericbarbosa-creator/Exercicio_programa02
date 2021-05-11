
import random

#E = espada
#C= Copas
#0 = Ouros
#P = Paus

def cria_baralho():
    lista = []
    numeros = ['1','2','3','4','5','6','7','8','9','10'] #lista de números
    naipe =['E','C','O','P']#lista de naipes
    numeros_embaralhados = random.choice(numeros)
    naipes_embaralhadas=random.choice(naipe)
    carta_embaralhadas = numeros_embaralhados+naipes_embaralhadas #concatenamento de strings
    lista.append(carta_embaralhadas)
    return lista

print(cria_baralho())


