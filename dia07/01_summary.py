# %%
import pandas as pd

idades = [32,44,12,54,67,32,23,34,32,12,45,43,28,73,29]
idades = pd.Series(idades)
#print(idades)
#print(idades.sum())#soma
#print(idades.min())#mostra o menor numero
#print(idades.max())#o maior numero
#print(idades.mean())# media de idades
#print(idades.describe()) #descreve o tipo de dados

# %%
clientes = pd.read_csv("../data/clientes.csv",sep=';')
#
#print(clientes)

# %%
#print(clientes["flTwitch"].sum())# mostra a agregaçao so desta serie
#print(clientes["flTwitch"].mean())
#print(clientes.columns)


redes_sociais = ["flEmail","flTwitch","flYouTube","flBlueSky","flInstagram"]
#print(clientes[redes_sociais].sum())#aplica a formula para o novo data frame

# %%
num_columns = clientes.dtypes[~(clientes.dtypes == "object")].index.tolist()#mostra as colunas do tipo float
#print(clientes[num_columns].mean())#media das colunas tipo float

# %%
#print(clientes[num_columns].describe())#descreve dertalhadamente cada coluna do tipo float

# %%
print(clientes[["flTwitch", "flEmail"]].describe())#descreve detalhadamente apeas estas colunas