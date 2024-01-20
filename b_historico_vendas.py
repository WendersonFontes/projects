import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

class DataAnalyzer:
    def __init__(self):
        self.csv_path = None
        self.merged_data = None

    def get_csv_file(self):
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(title="Selecione o arquivo CSV", filetypes=[("Arquivos CSV", "*.csv")])
        root.destroy()
        return file_path

    def read_csv_file(self):
        self.csv_path = self.get_csv_file()
        self.load_data()

    def load_data(self):
        data = pd.read_csv(self.csv_path)
        data['data'] = pd.to_datetime(data['data'])
        self.merged_data = data

    def plot_data(self):
        fig, ax = plt.subplots(figsize=(14, 8), facecolor='lightgray')  
        category_data = self.merged_data.pivot_table(index='data', columns=['categoria'], values='valor_venda_total', aggfunc='sum')
        category_colors = {'Produtos': 'blue', 'Serviços': 'brown'}

        category_data.plot(ax=ax, linestyle='-', marker='o', color=[category_colors[cat] for cat in category_data.columns])
        
        plt.title('Comparação de Vendas por Categoria ao longo do Tempo')
        plt.xlabel('Data')
        plt.ylabel('Valor de Venda Total')
        plt.legend(title='Categoria', loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, ncol=2)

        plt.xticks(rotation=45, ha='right')
        plt.grid(True, linestyle='--', alpha=0.6)

        for category in category_data.columns:
            max_value = category_data[category].max()
            min_value = category_data[category].min()

            max_index = category_data[category].idxmax()
            min_index = category_data[category].idxmin()

            month_max = max_index.strftime('%B')  
            month_min = min_index.strftime('%B')  

            ax.annotate(f'Máximo: {max_value:.2f} ({month_max})', xy=(max_index, max_value), xytext=(max_index, max_value + 200),
                        arrowprops=dict(facecolor=category_colors[category], shrink=0.05), color=category_colors[category])
            
            ax.annotate(f'Mínimo: {min_value:.2f} ({month_min})', xy=(min_index, min_value), xytext=(min_index, min_value - 200),
                        arrowprops=dict(facecolor=category_colors[category], shrink=0.05), color=category_colors[category])

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    analyzer = DataAnalyzer()
    analyzer.read_csv_file()
    analyzer.plot_data()
