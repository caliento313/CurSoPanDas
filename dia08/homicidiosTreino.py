import pandas as pd
#codigo para ler o dataframe
df = pd.read_csv("../data/ipea/homicidios.csv", sep=";")
#print(df.head())
df = df.rename(columns={'valor':'homicidios'})
#print(df)
#codigo para ler o dataframe
df_negros = pd.read_csv('../data/ipea/homicidios-negros.csv',sep=';')
#print(df_negros.head())
df_negros = df_negros.rename(columns={'valor':'homicidios'})
#print(df_negros)
#print(df_negros.dtypes)
#codigo para unir os datas frames lado a lado
df = df.set_index(['nome','período'])
df_negros = df_negros.set_index(['nome','período'])
dfmix = (pd.concat([df, df_negros], axis=1))
print(dfmix)

