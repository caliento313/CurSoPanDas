# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv",sep=';')
print(df.head())

# %%
#METODO PARA CRIAR UMA LISTA DE UMA STR DIVIDIR POR -  E PEGAR A ULTIMA POSIÇAO
def get_last_id(idCliente):
   return idCliente.split("-")[-1]

# %%

print(get_last_id("0033b737-8235-4c0f-9801-dc4ca185af00"))

# %%
#MANEIRA DE FAZER SEM USAR O PANDAS
id_novo = []

for i in df["idCliente"]:
    novo = get_last_id(i)
    id_novo.append(novo)

df["novo_id"] = id_novo
print(id_novo)
#df.head()

# %%
#USANDO O METODO APLY DA FUNÇAO CRIADA A CIMA
print(df["idCliente"].apply(get_last_id))



# %%
