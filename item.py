class item:

    def __init__(self, id, interest, weight):
        self.id = id
        self.interest = interest
        self.weight = weight

    # Cria uma lista de itens
    def getItems(path, size):
        # Arquivo que contém as informações dos itens utilizados
        arq = open(path, "r")

        # Lê a primeira linha do arquivo
        linha = arq.readline().split()

        # Cria uma lista vazia
        li = []
        
        # Percorre todo o arquivo, adicionando as informações de size itens do arquivo para a lista
        for i in range(size):
            linha = arq.readline().split()
            li.append(item(linha[0], linha[1], linha[2]))
        
        arq.close()
        return li


    # Ordena a lista de itens em ordem crescente com base na proporção interesse/peso
    def sortItems(itemsL):
        # Ordena a lista em ordem crescente
        itemsL = sorted(itemsL, key = lambda x: int(x.interest) / int(x.weight))

        return itemsL