import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv')

plt.figure(figsize=(10, 6))
sns.lineplot(x='dia', y='venda', data=df, marker='o', color='skyblue')
plt.title('Preço médio da gasolina em São Paulo - Julho 2021', fontsize=16)
plt.xlabel('Dia', fontsize=12)
plt.ylabel('Preço (R$)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(df['dia'])
plt.savefig('gasolina.png')