import pandas as pd

dados_df = pd.read_excel("produtos_ficticios.xlsx")

# Qual o produto mais caro e mais barato ?

maiscaro = dados_df.loc[dados_df['Preço'].idxmax()]
print(maiscaro)



maisbarato = dados_df.loc[dados_df['Preço'].idxmin()]