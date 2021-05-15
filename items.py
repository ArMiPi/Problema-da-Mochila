from random import randrange

# Limitantes para a geração dos interesses do itens da mochila
MIN_RAND_INTEREST = 20
MAX_RAND_INTEREST = 60

# Limitantes para a geração dos pesos dos itens da mochila
MIN_RAND_WEIGHT = 10
MAX_RAND_WEIGHT = 100

class items:

    def __init__(self, size):
        # Quantidade de items
        self.size = size

        self.interest = self.interests()
        self.weight = self.weights()

    def interests(self):
        # Lista para armazenar os interesses de cada item
        interestL = []

        # Preenche a lista com números aleatórios entre MIN_RAND_INTEREST e MAX_RAND_INTEREST
        for i in range(self.size):
            interestL.append(randrange(MIN_RAND_INTEREST, MAX_RAND_INTEREST))
    
        return interestL

    def weights(self):
        # Lista para armazenar os pesos de cada item
        weightsL = []

        # Preenche a lista com números aleatórios entre MIN_RAND_WEIGHT e MAX_RAND_WEIGHT
        for i in range(self.size):
            weightsL.append(randrange(MIN_RAND_WEIGHT, MAX_RAND_WEIGHT))
            
        return weightsL