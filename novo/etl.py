import csv

def ler_arquivo_csv(caminho_arquivo):
    dados = []
    with open(caminho_arquivo, 'r', newline='', encoding='utf-8-sig') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        # Iterar sobre as linhas do arquivo CSV
        for linha in leitor_csv:
            if linha:
                dados.append(linha)
    return dados

# Exemplo de uso da função
caminho_arquivo = 'novo/fatura-2023-12-25.csv'  # Substitua 'arquivo.csv' pelo caminho do seu arquivo CSV
dados_csv = ler_arquivo_csv(caminho_arquivo)
for linha in dados_csv:
    print(linha)