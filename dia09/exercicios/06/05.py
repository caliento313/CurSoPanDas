# %%
# 06.05 - Qual a média de transações / dia?

import pandas as pd

df = pd.read_csv("../../../data/transacoes.csv")
df.head()

# %%
df["dtDia"] = pd.to_datetime(df["dtCriacao"]).dt.date

summary = df.agg({
    "idTransacao": 'count',
    "dtDia": 'nunique',
})

transacoe_dia = summary["idTransacao"] / summary["dtDia"]
transacoe_dia

# %%
