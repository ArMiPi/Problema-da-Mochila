from time import time
from os import system

# Tempo limite, em segundos, para a execução do método exaustivo
MAX_TIME = 5

# Retorna a capacidade da mochila
def capacity(li):
    c = 0
    maior = 0

    # Realiza a soma do peso de todos os itens e armazena o valor do maior peso encontrado
    for i in li:
        c += int(i.weight)
        if int(i.weight) > maior:
            maior = int(i.weight)

    # Define um valor para a capacidade
    c = int(c / 2)

    # Se o valor determinado for menor que o valor do maior peso, esse valor de peso é somado ao valor determinado
    if c <= maior:
        c += maior

    return c

# Verifica se uma lista possui apenas 0 como elemento(s)
def isAllZero(li):
    for i in li:
        if i != 0:
            return False
    
    return True

# Retorna uma possibilidade para a mochila
def possibility(p, li, first, cap):
    # Percorre a lista da posição first até a posição 0
    for i in range(first, -1, -1):
        if(cap - int(cap / int(li[i].weight)) >= 0):
            p[i] = int(cap / int(li[i].weight))
            cap -= (p[i] * int(li[i].weight))
    return p

# Retorna o interesse total da possibiladade analisada
def possibInterest(p, li):
    pI = 0

    for i in range(len(p)):
        pI += p[i] * int(li[i].interest)

    return pI

# Resolve o problema da mochila pelo método exaustivo
def exaustivo(li):
    start = time()

    # Capacidade da mochila
    cap = capacity(li)

    # Lista para armazenar as possibilidades
    possib = [0] * len(li)
    possib = possibility(possib, li, len(li) - 1, cap)

    # Maior interesse
    bestInterest = 0
    # Lista indicando onde ocorre(m) o(s) maior(es) interesse(s)
    lbi = []

    now = time()
    # A execução termina quando toda as opções forem esgotadas ou quando se passarem MAX_TIME segundos
    while now - start < MAX_TIME and not isAllZero(possib):
        if possibInterest(possib, li) > bestInterest:
            del lbi[:]
            bestInterest = possibInterest(possib, li)
            lbi.append(possib)
        elif possibInterest(possib, li) == bestInterest:
            lbi.append(possib)
        now = time()
        system("cls")

    for i in li:
        print(str(i.id))
    print()
    print(possib)
    print(lbi)
    print("Capacity: " + str(capacity(li)))