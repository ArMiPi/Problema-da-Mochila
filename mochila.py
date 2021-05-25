from os import system
from time import time

# Tempo limite, em segundos, para a execução do método exaustivo
MAX_TIME = 7200

# Entrada:
#   li -> list -> Lista contendo as informações dos itens utilizados
# Saída:
#   c -> int -> Capacidade da mochila
# Descrição:
#   Calcula a capacidade total da mochila
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

# Entrada:
#   possib -> list -> Lista contendo uma possibilidade de preenchimento da mochila
# Saída:
#   int -> Posição do primeiro elemento diferente de 0
#   -1 -> Caso a lista não possua elemento com valor 0
# Descrição:
#   Retorna a primeira posição que armazena um valor não zero e subtrai 1 do valor armazenado
#   na posição, ou retorna -1 caso todos os valores sejam 0. A posição 0 não é analisada
def firstNotZero(possib):
    # Setta a posição 0 para 0 caso ela não o seja
    if possib[0] != 0:
        possib[0] = 0

    # Procura pela primeira posição != 0
    for i in range(1, len(possib)):
        if possib[i] != 0:
            possib[i] -= 1
            return i
    
    # Caso todas as posições de possib sejam 0
    return -1

# Entradas:
#   p -> list -> Lista contendo uma possibilidade de preenchimento da mochila
#   li -> list -> Lista contendo as informações dos itens utilizados
#   first -> int -> Posição inicial a ser considerada
#   cap -> int -> Capacidade da mocihla
# Descrição:
#   A partir da posiçãp first, a lista p é percorrida até a posição 0. p é preenchida de tal forma que
#   cada elemento p[i] = cap / li[i].weight, sendo li[i].weight o peso do item correspondente na lista li
#   cap é atualizado a medida que p é preenchida, e deve ser >= 0
def possibility(p, li, first, cap):
    # Reduz da capacidade total a quantidade utilizada pelos itens posteriores à first
    for i in range(first, len(p)):
        cap -= (p[i] * int(li[i].weight))

    temp = 0
    # Percorre a lista da posição first até a posição 0
    for i in range(first-1, -1, -1):
        temp = int(cap / int(li[i].weight))
        p[i] = temp
        cap -= (temp * int(li[i].weight))

        if cap <= 0:
            break


# Retorna o interesse total da possibiladade analisada
def possibInterest(p, li):
    pI = 0

    for i in range(len(p)):
        pI += p[i] * int(li[i].interest)

    return pI

# Entrada:
#   path -> string -> Local e nome do arquivo com as melhores possibilidades
#   li -> list -> Lista contendo as informações dos itens utilizados
# Descrição:
#   Resolve o problema da mochila pelo método exaustivo, armazenando em um arquivo .txt a(s) melhor(es) possibilidade(s)
#   encontradas para preencher a mochila, bem como o tempo de execução da função e o valor da(s) melhor(es)
#   possibilidade(s)
def exaustivo(path, li):
    # Flag marcando o tempo no qual a função foi chamada
    start = time()

    # Capacidade da mochila
    cap = capacity(li)

    # Lista para armazenar as possibilidades
    possib = [0] * len(li)
    possibility(possib, li, len(li), cap)

    # Variável para armazenar a primeira posição que possui um valor não zero
    fnz = 0

    # Maior interesse
    bestInterest = 0
    pI = 0

    # Flag marcando o tempo atual
    currentTime = time() - start

    # A execução termina quando toda as opções forem esgotadas ou quando se passarem MAX_TIME segundos
    while currentTime < MAX_TIME and fnz != -1:
        # Armazena o interesse total da possibilidade atual
        pI = possibInterest(possib, li)

        # Preenchimento da lista com a(s) melhor(es) possibilidade(s)
        if pI > bestInterest:
            bestInterest = pI
            arq = open(path, "w")
            arq.write("Best Interest: " + str(bestInterest) + "\n")
            arq.write(str(possib) + "\n")
            arq.close()
        elif pI == bestInterest:
            arq = open(path, "a")
            arq.write(str(possib) + "\n")
            arq.close()

        # Atualizar o vetor possib para analisar a próxima possibilidade
        fnz = firstNotZero(possib)
        possibility(possib, li, fnz, cap)

        # Atualização do tempo atual
        currentTime = time() - start
        print(currentTime)
        system("cls")

    arq = open(path, "a")
    arq.write("Tempo decorrido: " + str(currentTime) + " s")
    arq.close()