# %%

import pandas as pd
#o concat vc pode empilhar um em cima do outro ou pode colocar uma do lado do outro
df = pd.DataFrame({
    "cliente": [1,2,3,4,5],
    "nome": ["teo", "jose", "nah", "mah", "lah"],
})
#print(df)

df_02 = pd.DataFrame({
    "cliente": [6,7,8],
    "nome": ["kozato", "laura", "dan",],
    "idade":[32,29,31],
})
#print(df_02)

df_03 = pd.DataFrame({
    "idade": [32,34,19,54,33]
})
#print(df_03)

# %%

dfs = [df, df_02]

pd.concat(dfs, ignore_index=True)
#print(dfs)

# %%

df_03 = df_03.sort_values(by='idade').reset_index(drop=True)
print(df_03)

# %%

print(pd.concat([df, df_03], axis=1))