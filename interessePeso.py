import random
import numpy as np


# Valores mínimo e máximo para geração de interesses
MIN_INTEREST = 10
MAX_INTEREST = 100

# Valores mínimo e máximo para geração de interesses
MIN_WEIGHT = 10
MAX_WEIGHT = 100

# Entrada:
#   path -> string -> Local e nome do arquivo com os itens que serão utilizados
#   size -> int -> Quantidade de itens que serão utilizados
# Descrição:
#   Cria um arquivo indicado pelo path. Esse arquivo irá conter size itens com interesses de MIN_INTEREST a MAX_INTEREST, 
#   e pesos de MIN_WEIGHT a MAX_WEIGHT
def createItems(path, size):
    # Cria o arquivo
    arq = open(path, "w")

    # Gera size números inteiros aleatórios entre MIN_WEIGHT e MAX_WEIGHT
    rnd = np.random.randint(MIN_WEIGHT, MAX_WEIGHT, size)

    # Preenche o arquivo
    arq.write("ID Interest Weight")
    for i in range(size):
        arq.write("\n" + str(i) + " " +str(random.randrange(MIN_INTEREST, MAX_INTEREST)) + " " + str(rnd[i]))   
    arq.close()