import csv

path_file = "data/vendas.csv"

def read_csv(path_file: str) -> list[dict]:
    """
    Lê um arquivo CSV e retorna uma lista com os dados
    :param path_file: Caminho do arquivo
    :return: dicionario com os dados
    """

    data = []
    with open(path_file, "r") as file:
        reader = csv.DictReader(file)
        data = list(reader)
    print(data)  # Movido para dentro da função
    return data

print(read_csv(path_file))