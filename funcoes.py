import random
def rolar_dados(x):
    lista = []
    i = 1
    while i <= x:
        y = random.randint(1,6)
        lista.append(y)
        i += 1
    return lista

print(rolar_dados(5))