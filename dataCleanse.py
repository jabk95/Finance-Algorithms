import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(6,3), index =['a', 'b', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e','f','g','h'])

print(df['one'].isnull())

#print(df.fillna(0))

#print(df.fillna(method = 'pad'))

print(df.dropna())

df = pd.DataFrame({'one':[10,20,30,40,50,2000],
'two':[1000,0,30,40,50,60]})
print (df.replace({1000:10,2000:60}))
