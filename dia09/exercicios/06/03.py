# %%
# 06.03 - Qual usuário teve maior quantidade de pontos debitados?

import pandas as pd

transacoes = pd.read_csv("../../../data/transacoes.csv")
transacoes.head()

# %%

filtro = transacoes['qtdePontos'] < 0

(transacoes[filtro].groupby(by='idCliente')['qtdePontos']
                   .sum()
                   .sort_values(ascending=True)
                   .head(1))