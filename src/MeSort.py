def meSort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2

    esquerda = meSort(lista[:meio])
    direita = meSort(lista[meio:])

    return juntar(esquerda, direita)


def juntar(esquerda, direita):
    resultado = []

    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado