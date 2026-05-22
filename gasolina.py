
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = {
    'dia': [1,2,3,4,5,6,7,8,9,10],
    'venda': [5.11,5.14,5.09,5.07,5.08,5.13,5.12,5.15,5.17,5.19]
}

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
