# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv",sep=';')
#PARA VER QUAIS LINHAS DA COLUNA DtAtualizacao ESTA PRESENTE COM NaN
#print(clientes[clientes['DtAtualizacao'].isna()])

# %%
#RETIRA OS NaN DAS LINHAS
#clientes.dropna(how="any")

# %%

df = pd.DataFrame(
   {
        "nome": ["Téo", None, "Nah", "Marcio"],
        "idade": [None, None, 43, 52],
        "salario": [3453,4324,None,5423]})
#DROPA O NaN DAS COLUNAS ESCOLIDAS
print( df)
print('~~'*15)
#df=df.dropna(how="any", subset=["idade",'nome','salario'])
#print(df)

# %%
#PREENCHE O VALOR DA LINHA NA COLUNA DESEJADA
df["idade"] = df["idade"].fillna(0)
print(df)

# %%

#df.fillna({"nome": "alguem", "idade": 0})

# %%
#medias = df[['idade', 'salario']].mean()
#df.fillna(medias)

# %%

#df["idade"].fillna(df["idade"].mean()).mean()