import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

class AnaliseCSV:
    def __init__(self, arquivo_csv):
        self.df = pd.read_csv(arquivo_csv, delimiter=';')

    def gerar_grafico(self):
        
        self.df['Relacao'] = self.df['total_vendido'] / self.df['total_quantidade']

        self.df = self.df.sort_values(by='Relacao', ascending=False)
       
        plt.figure(figsize=(10, 6))
        plt.bar(self.df['produto'], self.df['Relacao'], color='blue')
        plt.xlabel('Produto')
        plt.ylabel('Relação (Valor Vendido / Quantidade Vendida)')
        plt.title('Relação entre Quantidade Vendida e Valor Vendido por Produto')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()

def selecionar_arquivo():
    root = Tk()
    root.withdraw()  # Oculta a janela principal do tkinter

    arquivo_csv = filedialog.askopenfilename(title="Selecione o arquivo CSV")
    return arquivo_csv

# Exemplo de uso
if __name__ == "__main__":
    arquivo_csv = selecionar_arquivo()
    
    if arquivo_csv:
        analise = AnaliseCSV(arquivo_csv)
        analise.gerar_grafico()
