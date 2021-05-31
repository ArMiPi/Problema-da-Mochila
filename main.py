from item import *
import mochila
import interessePeso

# Quantidade de itens que serão utilizados
NUM_ITEMS = 1000

# Número do teste que está sendo executado
teste = 10

# Local onde a lista de itens será salva
pathItems = "Testes/Mochilas/" + str(NUM_ITEMS) + "-Items/Mochila-" + str(teste) + "-Items.txt"

# Local onde a lista de melhores possbilidades será salva
pathBestInterests = "Testes/Mochilas/" + str(NUM_ITEMS) + "-Items/Mochila-" + str(teste) + "-BestInterests-Limitante.txt"

# Gera os itens aleatoriamente (ID/Interesse/Peso)
interessePeso.createItems(pathItems, NUM_ITEMS)

# Armazena os itens do txt em uma lista
li = item.getItems(pathItems, NUM_ITEMS)

# Ordena a lista em ordem crescente com base em (Interesse/Peso)
li = item.sortItems(li)

# Método exaustivo
mochila.exaustivo(pathBestInterests, li)
# Método com limitante superior
mochila.limitante(pathBestInterests, li)