import pandas as pd

#mostre os nomes e os preços dos produtos acima de 300 reais
dados_df = pd.read_excel("produtos_ficticios.xlsx")


caros = dados_df[dados_df['Preço'] > 300][['Nome do produto','Preço']]
print(caros)