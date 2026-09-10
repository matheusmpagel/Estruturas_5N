import time
from ListaRand import listaRand
from InSort import inSort

#=======================================================#

#Troque o '0' por quantos valores deseja inserir no algoritmo
qntValores = 0

#=======================================================#

inicio = time.perf_counter()

inSort(listaRand(qntValores))

fim = time.perf_counter()

tempo = fim - inicio

print(f"Tempo de execução: {tempo:.2f} segundos")


