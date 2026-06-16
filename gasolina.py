
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv("gasolina.csv")


gasolina = pd.DataFrame(dados)

gasolina.to_csv('gasolina.csv', index=False)

with sns.axes_style('whitegrid'):

    grafico = sns.lineplot(
        data=gasolina,
        x='dia',
        y='venda'
    )

    grafico.set_title('Preço médio da gasolina em São Paulo')
    grafico.set_xlabel('Dia')
    grafico.set_ylabel('Preço')

grafico.get_figure().savefig('gasolina.png')
