# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv",sep=';')
#print(transacoes.head())

# %%
clientes = pd.read_csv("../data/clientes.csv",sep=';')
#print(clientes.head())
#print(clientes.dtypes)

#print(transacoes.dtypes)
#tivemos que alterar o nome da coluna primaria porque estavam diferentes
transacoes=transacoes.rename(columns = {
    "IdCliente":"idCliente"})
#print(transacoes.dtypes)
#fizemos uma junçao das colunas usando a chave primaria como referencia idClientes
df = transacoes.merge(
    right=clientes,
    how='left',
    on=['idCliente'],
    suffixes=["Transacao", "Cliente"])
print(df)
print(df.dtypes)
# %%

#df_1 = pd.DataFrame({
 #   "transacao": [1,2,3,4,5],
  #  "nome": ["t1", "t2", "t3", "t4", "t5"],
   # "idCliente": [1,2,3,2,2],
    #"valor": [10,45,32,17,87],
#})

#df_2 = pd.DataFrame({
 #   "id": [1,2,3,4],
  #  "nome": ["teo", "nah", "mah", "jose"],
#})

#df_1.merge(
 #   df_2,
  #  left_on=["idCliente"],
   # right_on=["id"],
    #how='left',
    #suffixes=["Transacao", "Cliente"],
#)

# %%
