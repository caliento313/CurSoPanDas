# %%
#EXMPLO DE FILTROS
import pandas as pd

# %%

#pontos = [10, 1, 1, 1, 50, 100, 130, 30, 25, 50]
#filtro = []
#Exemplos de filtros usando o for
#valores_50_mais = []
#for i in pontos:
       #filtro.append(i>=50)
    #print(filtro)
#if i >= 50:
      #valores_50_mais.append(i)
#print(valores_50_mais)
#resultado = []
#for i in range(len(pontos)):
    #if filtro[i]:
        #resultado.append(pontos[i])
#print(resultado)
#filtro
# %%
#EXEMPLOS  de filtros USANDO O PANDAS
#brinquedo = pd.DataFrame(
    #{
        #"nome": ["teo", "nah", "mah"],
        #"idade": [32,35,14],
        #"uf": ["sp", "pr", "rj"],
     #}
#)
#print(brinquedo)
#FILTRA ELEMENTOS DA SERIE EM TRUE AND FALSE
#filtro = brinquedo["idade"] >= 18
#print(filtro)
#print(brinquedo[filtro])

# %%

df = pd.read_csv("../data/transacoes.csv", sep=";")
#print(df.head())
#print(df.columns)

# %%

# valores maiores que 50
#filtro = df['QtdePontos'] >= 50
#print(df[filtro])


# %%
# valores entre 50 (inclusive) e 100
#filtro = (df["QtdePontos"] >= 50) & (df["QtdePontos"] < 100)
#print(filtro)
#print(df[filtro])

# %%
#valores 1 e 100
#filtro = (df["QtdePontos"] == 1) | (df["QtdePontos"] == 100)
#print(df[filtro])

# %%
# pontos entre 0 e 50 ou do ano de 2025 para frente

filtro = (df["QtdePontos"] > 0) & (df["QtdePontos"]<=50) | (df["DtCriacao"]>='2025-01-01')
print(df[filtro])

# %%


#False or False = False