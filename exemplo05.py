from typing import List
# Calcular Desvio Padrão de uma Lista utilizando o import List
# from typing import List
# import math
# def calcular_desvio_padrao(valores: List[float]) -> float:
#     """
#     Calcula o desvio padrão de uma lista de valores
#     :param valores: Lista de valores
#     :return: Desvio padrão dos valores
#     """
#     media = sum(valores) / len(valores)
#     soma_diferencas_quadradas = sum((valor - media) ** 2 for valor in valores)
#     variancia = soma_diferencas_quadradas / len(valores)
#     desvio_padrao = math.sqrt(variancia)
#     return desvio_padrao
# valores = [10, 20, 30, 40, 50]
# desvio_padrao = calcular_desvio_padrao(valores)
# print(f"Desvio padrão dos valores: {desvio_padrao:.2f}")

def calcular_desvio_padrao(valores: List[float]) -> float:
    """
    Calcula o desvio padrão de uma lista de valores
    :param valores: Lista de valores
    :return: Desvio padrão dos valores
    """
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia ** 0.5

valores = [10, 20, 30, 40, 50]
desvio_padrao = calcular_desvio_padrao(valores)
print(f"Desvio padrão dos valores: {desvio_padrao:.2f}")

    
