from typing import List

# Filtrar Dados Acima de um Limite

# Exemplo 01
# def filtrar_acima_limite(lista, limite):
#     resultado = []
#     for valor in lista:
#         if valor > limite:
#             resultado.append(valor)
#     return resultado    

# numeros = [10, 20, 30, 40, 50]
# limite = 20
# valores_acima_limite = filtrar_acima_limite(numeros, limite)
# print("Valores acima do limite:", valores_acima_limite)

# Exemplo 02
def filtrar_acima_de(valores: List[float], limite: float) -> List[float]:
    """
    Filtra os valores acima do limite e retorna uma nova lista
    :param valores: Lista de valores
    :param limite: Limite para filtragem
    :return: Lista com os valores acima do limite
    """ 
    return [valor for valor in valores if valor > limite]

valores = [10, 20, 30, 40, 50]
limite = 30
valores_acima_limite = filtrar_acima_de(valores, limite)
print("Valores acima do limite:", valores_acima_limite)
  


