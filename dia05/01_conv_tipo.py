# %%

import pandas as pd

# %%

df = pd.read_csv("../data/clientes.csv",sep=';')
#print(df)

# %%
#CONVERTE O TIPO DE DADO FLOAT OU STR
#print(df["qtdePontos"].astype(float).astype(str))

# %%
print(df['DtCriacao'])

#CONVERTE AS DATAS EM FORMATO ERRADO EM UM VALIDO
replace = {"0000-00-00 00:00:00.000": "2024-02-01 09:00:00.000"}
#TRANSFORMA OS DADOS EM DATA
df["DtCriacao"] = pd.to_datetime(df["DtCriacao"].replace(replace))

# %%
#CONSIGO VER SOMENTE O MES
print(df["DtCriacao"].dt.month)