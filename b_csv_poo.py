import pandas as pd
from datetime import datetime, timedelta
import random

class GeradorDadosVendas:
    def __init__(self):
        self.inicio_ano = None
        self.fim_ano = None
        self.dados = []

    def obter_intervalo_anos(self):
        intervalo_anos = input("Digite o intervalo dos anos desejado (por exemplo, '2020-2023'): ")
        self.inicio_ano, self.fim_ano = map(int, intervalo_anos.split('-'))

        if self.inicio_ano < 1900 or self.fim_ano > 2100 or self.inicio_ano > self.fim_ano:
            raise ValueError("Intervalo de anos inválido.")

    def gerar_dados(self):
        for ano in range(self.inicio_ano, self.fim_ano + 1):
            for mes in range(1, 13):
                data_inicial = datetime(ano, mes, 1)
                ultimo_dia_mes = (data_inicial + timedelta(days=32)).replace(day=1) - timedelta(days=1)
                num_dias = (ultimo_dia_mes - data_inicial).days + 1

                for produto in ['Produtos', 'Serviços']:
                    valor_venda_total = sum(random.randint(800, 2500) for _ in range(num_dias))
                    self.dados.append([data_inicial, valor_venda_total, produto])

    def salvar_dados_csv(self):
        df = pd.DataFrame(self.dados, columns=['data', 'valor_venda_total', 'categoria'])
        df['data'] = df['data'].dt.to_period('M')

        nome_arquivo = input("Digite o nome do arquivo (ou pressione Enter para usar o padrão): ")

        if nome_arquivo == '':
            nome_arquivo = f'dados_vendas_{self.inicio_ano}_{self.fim_ano}_somatorio.csv'

        df.to_csv(nome_arquivo, index=False)
        print(f'Arquivo {nome_arquivo} gerado com sucesso.')

    def executar(self):
        try:
            self.obter_intervalo_anos()
            self.gerar_dados()
            self.salvar_dados_csv()

        except ValueError as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

gerador = GeradorDadosVendas()
gerador.executar()
