quantidadeAmigos = [5, 6, 4, 4, 2, 2, 4, 1, 6, 3, 2, 5, 4, 3, 1, 4]
conexoes = [12, 9, 8, 9, 4, 3, 9, 2, 10, 6, 3, 9, 11, 7, 4, 6]


def poximoAmigo(distancia, criancaId):
    amigoMaisProximo = []

    for idx, x in enumerate(conexoes):
        if idx != criancaId & distancia[idx] != 1:
            amigoMaisProximo.append(x - distancia[idx])

    max_value = max(amigoMaisProximo)
    return amigoMaisProximo.index(max_value)
