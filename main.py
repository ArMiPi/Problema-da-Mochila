from item import *
import mochila
import interessePeso

# Quantidade de itens que serão utilizados
NUM_ITEMS = 100

# Número do teste que está sendo executado
teste = 3

# Local onde a lista de itens será salva
pathItems = "Testes/Mochilas/" + str(NUM_ITEMS) + "-Items/Mochila-" + str(teste) + "-Items.txt"

# Local onde a lista de melhores possbilidades será salva
pathBestInterests = "Testes/Mochilas/" + str(NUM_ITEMS) + "-Items/Mochila-" + str(teste) + "-BestInterests-Exaustao.txt"

interessePeso.createItems(pathItems, NUM_ITEMS)

li = item.getItems(pathItems, NUM_ITEMS)

li = item.sortItems(li)

mochila.exaustivo(pathBestInterests, li)