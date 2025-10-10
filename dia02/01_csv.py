# %%
from operator import index

import pandas as pd
from pyarrow import parquet

df = pd.read_csv("../../data/clientes.csv")
#print(df)



# %%

#df.to_csv("clientes.csv", index=False)

# %%

df.to_parquet("clientes.parquet", index=False,)

# %%

df_2 = pd.read_parquet("../clientes.parquet")
print(df_2,sep=';')


# %%

#df.to_excel("clientes.xlsx", index=False)

# %%

#df_3 = pd.read_excel("clientes.xlsx")


# %%

#df_bobo = pd.read_csv("../data/bobo.csv", sep=";")

