from typing import List
# Encontrar Valores Ausentes em uma Sequência

def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    """
    Encontra os valores ausentes em uma sequência de números inteiros
    :param sequencia: Sequência de números inteiros
    :return: Lista com os valores ausentes
    """
    valores_ausentes = []
    for i in range(min(sequencia), max(sequencia) + 1):
        if i not in sequencia:
            valores_ausentes.append(i)
    return valores_ausentes
sequencia = [1, 2, 4, 5, 7]
valores_ausentes = encontrar_valores_ausentes(sequencia)
print("Valores ausentes:", valores_ausentes)