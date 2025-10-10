# %%

import pandas as pd
import requests


headers = {'User-Agent': 'Mozilla/5.0'}



url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
response = requests.get(url, headers=headers)
dfs = pd.read_html(response.text)


#print(dfs)
#print(len(dfs))

# %%

df_uf = dfs[1]
print(df_uf, sep=";")
#df_uf.to_csv("ufs.csv", sep=";", index=False)