import csv
from typing import List, Dict

def ler_csv(nome_arquivo: str) -> List[Dict[str, str]]:
    with open(nome_arquivo, 'r') as arquivo:
        leitor = csv.DictReader(arquivo)
        leitor.fieldnames = [name.strip() for name in leitor.fieldnames]
        return list(leitor)

def processar_dados(dados):
    categorias = {}
    for item in dados:
        categoria = item.get('Categoria', '').strip()
        if categoria:  # Only process if category is not empty
            if categoria not in categorias:
                categorias[categoria] = []
            categorias[categoria].append(item)
    return categorias

def calcular_total_vendas_categoria(dados):
    vendas_por_categoria = {}
    for categoria, itens in dados.items():
        total_vendas = 0
        for item in itens:
            quantidade = item.get('Quantidade', '0').strip() or '0'
            venda = item.get('Venda', '0').strip() or '0'
            try:
                total_vendas += float(quantidade) * float(venda)
            except (ValueError, TypeError):
                continue  # Skip invalid entries
        vendas_por_categoria[categoria] = total_vendas
    return vendas_por_categoria

def main():
    nome_arquivo = 'vendas.csv'
    dados_brutos = ler_csv(nome_arquivo)
    dados_processados = processar_dados(dados_brutos)
    vendas_categoria = calcular_total_vendas_categoria(dados_processados)
    for categoria, total in vendas_categoria.items():
        print(f"Total de vendas para a categoria {categoria}: R$ {total:.2f}")

if __name__ == "__main__":
    main()