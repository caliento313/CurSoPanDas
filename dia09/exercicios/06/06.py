# %%
# 06.06 - Como podemos calcular as estatísticas descritivas
# dos pontos das transações de cada usuário?

import pandas as pd

transacoes = pd.read_csv("../../../data/transacoes.csv")
transacoes.head()
# %%

(transacoes.groupby(by=['idCliente'], as_index=False)['qtdePontos']
           .describe())

