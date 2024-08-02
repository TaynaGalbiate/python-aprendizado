#Cartela de bingo com 12 números (4,3), os números variam de 1 e 30 e terá 10 participantes.

import numpy as np

bingo = np.random.randint(1, 31, size=(10, 4, 3)) #random.randint para colocar números aleatórios e inteiros, size é o tamanho

print(bingo)