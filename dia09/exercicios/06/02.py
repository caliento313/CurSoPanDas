# %%
# 06.02 - Quais são os usuários que mais fizeram transações?
# Considere os 10 primeiros.

import pandas as pd

df = pd.read_csv("../../../data/transacoes.csv")

(df.groupby(by=['idCliente'])['idTransacao']
   .count()
   .sort_values(ascending=False)
   .head(10))

