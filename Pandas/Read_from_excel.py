import pandas as pd

i = 0
k = 0
df = pd.read_excel('nmrv.xlsx')

nmrv = set(df['name'].tolist())

nmrv_p = df.loc[df['name'] == 'nmrv-p']
size = nmrv_p.loc[nmrv_p['size'] == 75]
print(size)
