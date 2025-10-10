# %%

import pandas as pd
from lxml.html.builder import SELECT

df = pd.read_csv("../data/transacoes.csv")
#print(df)
df = pd.read_csv("../data/transacoes.csv", sep=";")
#print(df)

# %%
#print(df.shape)

# %%
#print(df.info(memory_usage="deep"))

# %%
#Mostra as colunas e os tipos
#print(df.dtypes)

# %%
# renomear colunas
df=df.rename(columns = {
    "QtdePontos": "qtPontos",
    "DescSistemaOrigem": "SistemaOrigem"})
#print(df)

#print(df.dtypes)




# %%
#Para mostrar apenas duas colunas

#print(df [["IdCliente", "qtPontos"]])
#print(df.colunas)


#SELECT * from df
#print(df)

# %%
#CODIGOS RELACIONADOS COM O SELECT
# SELECT idCliente FROM df
#print(df[["IdCliente"]])

# %%

# SELECT idCliente, qtPontos FROM df LIMIT 5
#print(df[["IdCliente", "qtPontos"]].tail(5))

# %%

# SELECT idCliente, idTransacao, qtPontos
# FROM df
# LIMIT 5

#df[["idCliente", "idTransacao", "qtPontos"]].head(5)

# %%

colunas = list(df.columns)
colunas.sort()
print(colunas)

df = df[colunas]
print(df)
