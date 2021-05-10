
import random

#E = espada
#C= Copas
#0 = Ouros
#P = Paus

def cria_baralho():
    lista = []
    numeros = ['1','2','3','4','5','6','7','8','9','10']
    naipe =['E','C','O','P']
    numeros_embaralhados = random.choice(numeros)
    naipes_embaralhadas=random.choice(naipe)
    carta_embaralhas = numeros_embaralhados+naipes_embaralhadas
    lista.append(carta_embaralhas)
    return lista

x = dict(cria_baralho())

print(x)
print(type(x))
for chave, valor in x.items():
    print(chave)




