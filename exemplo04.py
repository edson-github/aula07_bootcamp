from typing import List
# Converter Celsius para Fahrenheit em uma Lista

def converter_celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
    """
    Converte uma temperatura em Celsius para Fahrenheit
    :param celsius: Temperatura em Celsius
    :return: Temperatura em Fahrenheit
    """
    fahrenheit = [(celsius * 9/5) + 32 for celsius in temperaturas_celsius]
    return fahrenheit

temperaturas_celsius = [0, 10, 20, 30, 40]
temperaturas_fahrenheit = converter_celsius_para_fahrenheit(temperaturas_celsius)
print("Temperaturas em Fahrenheit:", temperaturas_fahrenheit)