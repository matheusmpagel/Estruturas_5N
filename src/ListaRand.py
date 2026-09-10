import random

random.seed(42)

def listaRand(tamanho):
    return [random.randint(1, 1000) for _ in range(tamanho)]
