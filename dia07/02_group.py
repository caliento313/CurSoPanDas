# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv",sep=';')
#print(transacoes.head())

# %%
#print(transacoes.groupby(by=["IdCliente"]).count())

#print(transacoes.groupby(by=["IdCliente"])[["IdTransacao"]].count())#retorna uma dataframe com IdCliente como indice e apenas uma coluna IdTransacao

#print(transacoes.groupby(by=["IdCliente"], as_index=False)[["IdTransacao"]].count())#cria um indice para as duas colunas selecionadas

# %%
# qtde_transacoes
# total_pontos
# pontos / transacoes
#mostra as colunas e suas subcolunas
summary = (transacoes.groupby(by=["IdCliente"], as_index=False).agg({"IdTransacao": ['count'],"QtdePontos": ['sum', 'mean']}))

print(summary)

# %%
#print(summary[('QtdePontos','mean')])

#transforma aquelas subcolunas em colunas para melhor visualizacao
summary.columns = ['idCliente', 'qtdeTransacao', "totalPontos", "avgPontos"]
print(summary)