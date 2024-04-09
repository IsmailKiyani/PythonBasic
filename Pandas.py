import numpy as np
import pandas as pd

data = {'state':['Sindh','Sindh','Sindh','Punjab','Punjab','Punjab'],
       'year':[2000,2001,2002,2001,2002,2003],
       'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}
frame = pd.DataFrame(data)

frame.head()
frame.tail()

pd.DataFrame(data, columns=['year','state','pop'])

frame2 = pd.DataFrame(data, columns =['year','state','pop','debt'],
                     index=['one','two','three','four','five','six'])
frame2

frame2['state']

frame2.loc['three']

frame2['debt']=16.5
frame2

frame2['debt'] =np.arange(6.)
frame2

val = pd.Series([-1.2,-1.5,-1.7],index=['two','four','five'])
frame2['debt'] =val
frame2

frame2['South'] = frame2.state == 'Sindh'
frame2

del frame2['South']
frame2

frame2.columns

pop = {'Punjab':{2001: 2.4, 2002: 2.9},
      'Sindh':{2000: 1.5, 2001: 1.7, 2002: 3.6}}
pop

frame3 = pd.DataFrame(pop)
frame3

frame3.T

pdata = {'Sindh': frame3['Sindh'][:-1],
        'Punjab': frame3['Punjab'][:2]}
pd.DataFrame(pdata)

obj3 = pd.Series(['blue','purple','yellow'], index=[0,2,4])
obj3

obj3.reindex(range(6),method='ffill')

frame = pd.DataFrame(np.arange(9).reshape((3,3)),
                    index=['a','c','d'],
                    columns=['Sindh','KPK','Balochistan'])
frame

data = pd.DataFrame(np.arange(16).reshape((4,4)),
                   index=['Sindh','KPK','Balochistan','Punjab'],
                   columns=['one','two','three','four'])
data

data.drop(['Sindh','Balochistan'])

data.drop('two',axis=1)

data.drop(['two','four'],axis='columns')

obj = pd.Series(np.arange(4.),index=['a','b','c','d'])
obj

obj['b']

obj['b':'c']

obj['b','c']=5

obj

"""## Selection with loc nad iloc"""

data = pd.DataFrame(np.arange(16).reshape((4,4)),
                   index=['Balochistan','Sindh','Punjab','KPK'],
                   columns=['one','two','three','four'])
data

data.loc['Balochistan',['two','three']]

data.iloc[2,[3,0,1]]

data.iloc[2]

data.loc[:'Punjab','two']

data.iloc[:,:3][data.three > 5]

df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)),
                   columns=list('abcd'))
df1

df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)),
                   columns=list('abcde'))
df2

df2.loc[1, 'b'] = np.nan
df2

df1 + df2

df1.add (df2, fill_value=0)

1/ df1

df2.rdiv(1)

df1.count()

df1.describe().mean()

df1.mean()

df1.median()

df1.mad()

df1.prod()

df1.var()

df1.skew()

df1.kurt()

df1.cumsum()

"""## Data loading, Storage, and File Formats"""

df = pd.read_csv('test.csv')
df

df.head()

df.describe()

"""## Data Cleaning and Preparation"""

string_data = pd.Series(['aardvark','artichoke',np.nan,'avocado'])
string_data

string_data.describe()

string_data.isnull()

from numpy import nan as NA

data = pd.Series([1, NA, 3.5, NA,7])
data

data.dropna()

data[data.notnull()]

data = pd.DataFrame([[1.,6.5,3.],[1.,NA,NA],
                    [NA,NA,NA],[NA,6.5,3.]])
data

cleaned = data.dropna()
data

cleaned

data[4]= NA

data.dropna(axis=1, how='all')
data

"""## Data Cleaning and Preparation"""

string_data = pd.Series(['aardvark','artichoke', np.nan, 'avocado'])
string_data

string_data.isnull()

"""## Permutation and random sampling"""

df = pd.DataFrame(np.arange(5 * 4).reshape((5,4)))
df

sampler = np.random.permutation(5)
sampler

df.take(sampler)

df.sample(n=3)

choices = pd.Series([5,7,-1,6,4])
choices

draws = choices.sample(n=10, replace=True)
draws