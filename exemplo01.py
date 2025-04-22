# Calcular Média de Valores em uma Lista

def calcular_media(lista):
    if len(lista) == 0:
        return 0
    soma = sum(lista)
    media = soma / len(lista)
    return media
numeros = [10, 20, 30, 40, 50]
media = calcular_media(numeros)
print("A média dos números é:", media)
