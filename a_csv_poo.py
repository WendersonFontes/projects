import csv
import random
from datetime import datetime, timedelta

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Venda:
    def __init__(self, produto, data, quantidade):
        self.produto = produto
        self.data = data
        self.quantidade = quantidade
        self.preco_unitario = produto.preco
        self.total = quantidade * self.preco_unitario

    def to_csv_row(self):
        return [self.data.strftime("%Y-%m-%d %H:%M:%S"), self.produto.nome, self.quantidade, self.preco_unitario, self.total]

def random_date(start_date, end_date):
    return start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

# Lista de produtos
produtos = [
    Produto("Caneta", 2.5),
    Produto("Caderno", 10.0),
    Produto("Lapis", 1.0),
    Produto("Borracha", 1.5),
    Produto("Regua", 3.0),
    Produto("Papel A4", 5.0),
    Produto("Cola", 2.0),
    Produto("Tesoura", 4.0),
    Produto("Apontador", 1.2),
    Produto("Estojo", 6.5),
    Produto("Marcador", 3.5),
    Produto("Grampeador", 8.0),
    Produto("Quadro Negro Eletronico", 50.0),
    Produto("Calculadora Cientifica", 25.0),
    Produto("Mochila", 20.0),
    Produto("Post-its", 3.0),
    Produto("Lancheira", 15.0),
    Produto("Tinta Acrilica", 7.0),
    Produto("Mapa Mundi", 18.0),
    Produto("Giz de Cera", 2.0),
    Produto("Lupa", 12.0),
    Produto("Fita Adesiva", 1.8),
]


# Configuração do período de vendas (1 ano)
data_inicio = datetime(2023, 1, 1)
data_fim = datetime(2023, 12, 31)

# Nome do arquivo CSV
nome_arquivo = "vendas_papelaria.csv"

# Lista para armazenar as instâncias de Venda
vendas = []

# Gerar dados de vendas variáveis para cada produto
for produto in produtos:
    for _ in range(365):
        data_venda = random_date(data_inicio, data_fim)
        quantidade = random.choices([0, 1, 2, 3, 4, 5], weights=[0.2, 0.3, 0.2, 0.1, 0.1, 0.1])[0]
        venda = Venda(produto, data_venda, quantidade)
        vendas.append(venda)

# Abrir o arquivo CSV para escrita
with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    
    # Escrever o cabeçalho no arquivo
    escritor_csv.writerow(["Date", "Produto", "Quantidade", "Preco Unitario", "Total"])
    
    # Escrever os dados de venda no arquivo
    for venda in vendas:
        escritor_csv.writerow(venda.to_csv_row())

print(f"Arquivo {nome_arquivo} gerado com sucesso.")
