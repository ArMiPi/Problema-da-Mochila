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
        # Quantidade do item li[i] que pode ser inserida na mochila
        temp = int(cap / int(li[i].weight))
        p[i] = temp
        # Capacidade restante na mochila
        cap -= (temp * int(li[i].weight))

        if cap <= 0:
            break


# Entradas:
#   p -> list -> Lista contendo uma possibilidade de preenchimento da mochila
#   li -> list -> Lista contendo as informações dos itens utilizados
# Saída:
#   int -> Interesse total da possibilidade analisada
# Descrição:
#   Retorna o interesse total da possibiladade analisada
def possibInterest(p, li):
    pI = 0

    # Soma de interesse * quantidade de itens para cada item da lista
    for i in range(len(p)):
        pI += p[i] * int(li[i].interest)

    return pI

# Entradas:
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
        print(possib)
        # Preenchimento da lista com a(s) melhor(es) possibilidade(s)
        # Substitui os dados armazenados em path por possib
        if pI > bestInterest:
            bestInterest = pI
            arq = open(path, "w")
            arq.write("Best Interest: " + str(bestInterest) + "\n")
            arq.write(str(possib) + "\n")
            arq.close()
        # Adiciona possib à path
        elif pI == bestInterest:
            arq = open(path, "a")
            arq.write(str(possib) + "\n")
            arq.close()

        # Atualizar o vetor possib para analisar a próxima possibilidade
        fnz = firstNotZero(possib)
        possibility(possib, li, fnz, cap)

        # Atualização do tempo atual
        currentTime = time() - start

    # Salva em path o tempo de execução da função
    arq = open(path, "a")
    arq.write("Tempo decorrido: " + str(currentTime) + " s")
    arq.close()

# Entradas:
#   possib -> list -> Lista contendo uma possibilidade de preenchimento da mochila
#   li -> list -> Lista contendo as informações dos itens utilizados
#   first -> int -> Posição inicial a ser considerada
#   cap -> int -> Capacidade da mocihla
# Saída:
#   double -> Limitante Superior
#  Descrição:
#   Calcula um limitante superior da seguinte forma:
#   ls = (somatório[i = first, len(possib)] li[i].interest*possib[i]) + 
#   ((li[first-1].interest)/li[first-1].weight) * (cap - (somatório[i = first, len(possib)] int(li[i].weight) * possib[i]))
def limitanteSuperior(possib, li, first, cap):
    # somatório[i = first, len(possib)] li[i].interest*possib[i]
    lim = 0
    for i in range(first, len(possib)):
        lim += (int(li[i].interest) * possib[i])
    
    # somatório[i = first, len(possib)] li[i].weight * possib[i])
    lp = 0
    for i in range(first, len(possib)):
        lp += (int(li[i].weight) * possib[i])
    
    lim += (int(li[i-1].interest) / int(li[i-1].weight)) * (cap - lp)

    return lim

# Entradas:
#   path -> string -> Local e nome do arquivo com as melhores possibilidades
#   li -> list -> Lista contendo as informações dos itens utilizados
# Descrição:
#   Resolve o problema da mochila utilizando um limitante superior, armazenando em um arquivo .txt a(s) melhor(es) possibilidade(s)
#   encontradas para preencher a mochila, bem como o tempo de execução da função e o valor da(s) melhor(es)
#   possibilidade(s)
def limitante(path, li):
    # Flag marcando o tempo no qual a função foi chamada
    start = time()

    # Capacidade da mochila
    cap = capacity(li)

    # Lista para armazenar as possibilidades
    possib = [0] * len(li)
    possibility(possib, li, len(li), cap)
    
    # Maior interesse
    bestInterest = possibInterest(possib, li)
    pI = 0

    arq = open(path, "w")
    arq.write("Best Interest: " + str(bestInterest) + "\n")
    arq.write(str(possib) + "\n")
    arq.close()

    # Variável para armazenar a primeira posição que possui um valor não zero
    fnz = firstNotZero(possib)

    # A execução termina quando toda as opções forem esgotadas ou quando se passarem MAX_TIME segundos
    while fnz != -1:
        if limitanteSuperior(possib, li, fnz, cap) >= bestInterest:
            possibility(possib, li, fnz, cap)

            pI = possibInterest(possib, li)

            print(possib)
            print("Limitante = " + str(limitanteSuperior(possib, li, fnz, cap)))
            # Preenchimento da lista com a(s) melhor(es) possibilidade(s)
            # Substitui os dados armazenados em path por possib
            if pI > bestInterest:
                bestInterest = pI
                arq = open(path, "w")
                arq.write("Best Interest: " + str(bestInterest) + "\n")
                arq.write(str(possib) + "\n")
                arq.close()
            # Adiciona possib à path
            elif pI == bestInterest:
                arq = open(path, "a")
                arq.write(str(possib) + "\n")
                arq.close()
        # Zera a posição fnz de possib caso fnz não seja a última posição
        if fnz != (len(possib) -1):
            possib[fnz] = 0
        fnz = firstNotZero(possib)
        
    # Tempo de execução da função
    currentTime = time() - start
    arq = open(path, "a")
    arq.write("Tempo decorrido: " + str(currentTime) + " s")
    arq.close()