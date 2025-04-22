# Contar Valores Únicos em uma Lista

def contar_valores_unicos(lista):
    valores_unicos = set(lista)
    return len(valores_unicos)
numeros = [1, 2, 3, 5, 6, 5, 6, 6, 7]
quantidade_unicos = contar_valores_unicos(numeros)
print("Quantidade de valores únicos:", quantidade_unicos)

