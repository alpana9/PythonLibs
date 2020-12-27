
import pandas as pd

import numpy as np

#Lsts see what is DataFrames -- should be more than 1 row and more than 1 column
# DataSeries --can be one row or one column

df = pd.DataFrame(np.arange(0,20).reshape(5,4), index = ['Row1', 'Row2', 'Row3', 'Row4', 'Row5'], columns = ["Column1", "Column2", "Column3", "Column4"])

df.head()
Out[5]: 
      Column1  Column2  Column3  Column4
Row1        0        1        2        3
Row2        4        5        6        7
Row3        8        9       10       11
Row4       12       13       14       15
Row5       16       17       18       19

df.loc['Row2']
Out[8]: 
Column1    4
Column2    5
Column3    6
Column4    7
Name: Row2, dtype: int32

type(df.loc['Row2'])
Out[9]: pandas.core.series.Series

type(df.loc['Row2':, 'Column2'])
Out[12]: pandas.core.series.Series

df.loc['Row2':, 'Column2']
Out[13]: 
Row2     5
Row3     9
Row4    13
Row5    17
Name: Column2, dtype: int32

df.loc['Row2':, 'Column2':]
Out[14]: 
      Column2  Column3  Column4
Row2        5        6        7
Row3        9       10       11
Row4       13       14       15
Row5       17       18       19

type(df.loc['Row2':, 'Column2':])
Out[15]: pandas.core.frame.DataFrame


df.loc[:,:]
Out[16]: 
      Column1  Column2  Column3  Column4
Row1        0        1        2        3
Row2        4        5        6        7
Row3        8        9       10       11
Row4       12       13       14       15
Row5       16       17       18       19

df.iloc[:,:]  #index location, it requires both row and column indexs unlike loc
Out[17]: 
      Column1  Column2  Column3  Column4
Row1        0        1        2        3
Row2        4        5        6        7
Row3        8        9       10       11
Row4       12       13       14       15
Row5       16       17       18       19

df.iloc[:,:].values
Out[18]: 
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19]])

df.loc[:,:].values

Out[19]: 
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11],
       [12, 13, 14, 15],
       [16, 17, 18, 19]])
       
       df['Column2'].value_counts()
Out[20]: 
13    1
5     1
17    1
9     1
1     1
Name: Column2, dtype: int64


df.to_csv('Test1.csv')
type(df.iloc[0:2,0])
Out[27]: pandas.core.series.Series

type(df.iloc[0:2,0:1])
Out[28]: pandas.core.frame.DataFrame
df.iloc[0:2,0:1]
Out[29]: 
      Column1
Row1        0
Row2        4

df.iloc[0:2,0]
Out[30]: 
Row1    0
Row2    4
Name: Column1, dtype: int32

df.iloc[:,1:].values.shape
Out[34]: (5, 3)

df.isnull()
Out[35]: 
      Column1  Column2  Column3  Column4
Row1    False    False    False    False
Row2    False    False    False    False
Row3    False    False    False    False
Row4    False    False    False    False
Row5    False    False    False    False

df.isnull().sum()
Out[36]: 
Column1    0
Column2    0
Column3    0
Column4    0
dtype: int64


df
Out[37]: 
      Column1  Column2  Column3  Column4
Row1        0        1        2        3
Row2        4        5        6        7
Row3        8        9       10       11
Row4       12       13       14       15
Row5       16       17       18       19

df['Column1'].unique()
Out[38]: array([ 0,  4,  8, 12, 16], dtype=int64)

df[['Column1','Column4']]    #multiple column , put it in list
Out[40]: 
      Column1  Column4
Row1        0        3
Row2        4        7
Row3        8       11
Row4       12       15
Row5       16       19

