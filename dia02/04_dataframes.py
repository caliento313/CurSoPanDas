# %%

import pandas as pd

# para ler um documento
df_clientes = pd.read_csv("../../data/clientes.csv")
#print(df_clientes)
import pandas as pd

df = pd.read_csv("../../data/clientes.csv", sep=";")
#print(df)
import pandas as pd
#para mostrar todas as linhas e colunas

pd.set_option('display.max_rows', None)  # Mostra todas as linhas
pd.set_option('display.max_columns', None)  # Mostra todas as colunas

#print(df)


# %%
## AMOSTRAS
#para ler as 10 primeiras linhas

print(df.head(n=10))

# %%
#para ler as ultimas linhas
#print(df_clientes.tail(10))

# %%
#para ler aliatorio
#print(df_clientes.sample(10))

# %%
#para descobrir quantas linhas e colunas tem
 #print(df_clientes.shape)

# monstra as colunas
#print(df_clientes.columns)

# para mostrar o range
#print(df_clientes.index)

# informaçoes sobre a tabela como a memoria
#print(df_clientes.info(memory_usage='deep', max_cols=2))
#
# %%
#print(df_clientes.dtypes)