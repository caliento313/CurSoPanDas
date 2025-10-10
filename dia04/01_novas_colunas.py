# %%

import pandas as pd
import numpy as np

df = pd.read_csv("../../data/clientes.csv", sep=';')
#print(df.head())

# %%
#ADD 100 PONTOS A COLUNA qtDEPONTOS
#print(df["qtdePontos"] +100)
#print(df["qtdePontos"] )

#CRIOU UMA NOVA VOLUNA COM OS PONTOS ADD

#df["pontos_100"] = df["qtdePontos"] + 100
#print(df.head())

# %%

#nova_coluna = []
#for i in df["qtdePontos"]:
 #   nova_coluna.append( i+100)
#print(nova_coluna)



# %%
#CRIOU UMA NOVA COLUNA ATRAVEZ DAS DUAS ANTIGAS flEmail , flTwitch
df["emailTwitch"] = df["flEmail"] + df["flTwitch"]
#print(df.head())

# %%
#print(df["flEmail"] * df["flTwitch"])

# %%
#ME DIZ QUANTAS MIDIAS SOCIAS TEM
df["qtdeSocial"] = df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"]
#print(df)

# %%
#MOSTRA SE TEM TODSAS AS MEDIAS SOCIAS CASO CONTRARIO = 0
df["todas_social"] = df["flEmail"] * df["flTwitch"] * df["flYouTube"] * df["flBlueSky"] * df["flInstagram"]
#print(df)

# %%
#print(df["qtdePontos"].describe())

# %%
#PARA FAZER TRANSFORMAÇOES DE DADOS COMO LOG TANGENTI ARCO COSENO
df["logPontos"] = np.log(df["qtdePontos"]+1)
#print(df['logPontos'])
#print(df["logPontos"].describe())

# %%
#FORMAÇAO DE GRAFICOS
from matplotlib import pyplot as plt

print(plt.grid(True))
print(plt.hist(df["logPontos"]))
print(plt.show())