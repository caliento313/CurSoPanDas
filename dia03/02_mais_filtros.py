# %%
import pandas as pd

df = pd.read_csv("../data/transacao_produto.csv", sep=";")
#print(df)

# %%
#filtra o id do produto
#filtro = (df["IdProduto"] == 5) | (df["IdProduto"] == 11)
#print(df[filtro])

# %%
#formula pandas para filtrob id do produto
#filtro = df["IdProduto"].isin([5,11])
#print(df[filtro])

# %%

clientes = pd.read_csv("../../data/clientes.csv", sep=";")
#print(clientes.head())
#mostra as afirmasoes verdadeiras e falças
filtro1 = clientes["DtCriacao"].isna()
filtro2 = clientes['DtCriacao'].notna()

print(~clientes[filtro1])
print(clientes[filtro2])
# %%

#print(clientes["DtCriacao"].isna())
#print(clientes["DtCriacao"].notna())