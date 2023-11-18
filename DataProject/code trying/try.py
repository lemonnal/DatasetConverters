import pandas as pd
import numpy as np

L = [range(10),
     range(7),
     range(34),
     range(10)]

df = pd.DataFrame(L)
df = df.fillna(-1).astype(int).astype(str).replace('-1', np.nan)

print(df)

df.to_csv('try.txt', sep=' ', header=None, index=False)
