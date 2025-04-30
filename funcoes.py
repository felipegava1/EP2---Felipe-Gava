import random
def rolar_dados(x):
    lista = []
    i = 1
    while i <= x:
        y = random.randint(1,6)
        lista.append(y)
        i += 1
    return lista

def guardar_dado(dados_rolados, dados_no_estoque, dados_para_guardar):
    novo = []
    sublista1 = []
    sublista2 = []
    dados_no_estoque.append(dados_rolados[dados_para_guardar])
    del dados_rolados[dados_para_guardar]
    for i in range(len(dados_rolados)):
        sublista1.append(dados_rolados[i])
    novo.append(sublista1)
    for i in range(len(dados_no_estoque)):
        sublista2.append(dados_no_estoque[i])
    novo.append(sublista2)
    return novo

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    novo = []
    sublista1 = []
    sublista2 = []
    dados_rolados.append(dados_no_estoque[dado_para_remover])
    del dados_no_estoque[dado_para_remover]
    for i in range(len(dados_rolados)):
        sublista1.append(dados_rolados[i])
    novo.append(sublista1)
    for i in range(len(dados_no_estoque)):
        sublista2.append(dados_no_estoque[i])
    novo.append(sublista2)
    return novo

def calcula_pontos_regra_simples(lista):
    dic = {}
    i = 1
    while i < 7:
        dic[i] = 0
        i += 1
    for j in range(len(lista)):
        dado = lista[j]
        dic[dado] += dado
    return dic

def calcula_pontos_soma(lista):
    pontos = 0
    for i in range(len(lista)):
        pontos += lista[i]
    return pontos

def calcula_pontos_sequencia_baixa(lista):
    sequencia = False
    if 1 in lista and 2 in lista and 3 in lista and 4 in lista:
        sequencia = True
    if 2 in lista and 3 in lista and 4 in lista and 5 in lista:
        sequencia = True
    if 3 in lista and 4 in lista and 5 in lista and 6 in lista:
        sequencia = True
    if sequencia == True:
        return 15
    else:
        return 0

def calcula_pontos_sequencia_alta(lista):
    sequencia_alta = False
    if 1 in lista and 2 in lista and 3 in lista and 4 in lista and 5 in lista:
        sequencia_alta = True
    if 6 in lista and 2 in lista and 3 in lista and 4 in lista and 5 in lista:
        sequencia_alta = True
    if sequencia_alta == True:
        return 30
    else:
        return 0
    
def calcula_pontos_full_house(lista):
    dic = {}
    for i in range(len(lista)):
        if lista[i] in dic:
            dic[lista[i]] += 1
        else:
            dic[lista[i]] = 1   
    if 2 in dic.values() and 3 in dic.values():
        fullhouse = True
    else:
        fullhouse = False
    if fullhouse:
        pontos = 0
        for i in range(len(lista)):
            pontos += lista[i]
        return pontos
    else: 
        return 0

def calcula_pontos_quadra(lista):
    dic = {}
    for i in range(len(lista)):
        if lista[i] in dic:
            dic[lista[i]] += 1
        else:
            dic[lista[i]] = 1 
    quadra = False
    for x in dic.values():
        if x >= 4:
            quadra = True
    if quadra:
        pontos = 0
        for i in range(len(lista)):
            pontos += lista[i]
        return pontos 
    else: 
        return 0