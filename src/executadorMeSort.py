import time
from ListaRand import listaRand, listaOrd
from MeSort import meSort

#=======================================================#

#Troque o '0' por quantos valores deseja inserir no algoritmo
qntValores = 0

#=======================================================#

aleatorio = listaRand(qntValores)
ordenado = listaOrd(aleatorio)

inicio_al = time.perf_counter()
meSort(aleatorio)
fim_al = time.perf_counter()
tempo_al = fim_al - inicio_al

inicio_or = time.perf_counter()
meSort(ordenado)
fim_or = time.perf_counter()
tempo_or = fim_or - inicio_or

print(f"Tempo de execução da lista aleatória: {tempo_al:.9f} segundos")
print(f"Tempo de execução da lista ordenada: {tempo_or:.9f} segundos")

#*Reduza o .9f caso queira menos casas decimais