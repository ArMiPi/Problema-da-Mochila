from item import *
import mochila
import interessePeso

interessePeso.createItems("Items.txt", 10)

li = item.getItems("Items.txt", 10)

for i in li:
    print("ID: "+str(i.id))
    print("Interesse: "+str(i.interest))
    print("Peso: "+str(i.weight))
    print()

li = item.sortItems(li)

mochila.exaustivo(li)

#del x.weight[:]

#print(x.weight)