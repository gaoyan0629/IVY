# pandas cell level access and unicode handling
for column in df.columns:
    for idx in df[column].index:
        x = df.get_value(idx,column)
        try:
            x = unicode(x.encode('utf-8','ignore'),errors ='ignore') if type(x) == unicode else unicode(str(x),errors='ignore')
            df.set_value(idx,column,x)
        except Exception:
            print 'encoding error: {0} {1}'.format(idx,column)
            df.set_value(idx,column,'')
            continue

fn = u'filename\u4500abc'
f = open(fn, 'w')
f.close()
0–1,114,111 (0x10ffff in base-16)
For example, the character encoding scheme ASCII comprises 128 code points in the range 0hex to 7Fhex, 


# reset index
df = pd.DataFrame(np.random.random((200,3)))
df['date'] = pd.date_range('2000-1-1', periods=200, freq='D')
df = df.set_index(['date'])
print(df.loc['2000-6-1':'2000-6-10'])



## initialize an index array
    idx = np.asarray([])

    ## initialize an array for columns
    cols = np.asarray([])

    ## loop thru the query resultset to make up the DataFrame
    for r in result:
        idx = np.append(idx, [r.price_time])
        cols = np.append(cols, [r.open_price, r.high_price, \r.low_price, r.close_price, r.volume])

    ## reshape the 1-D array into a 2-D array for each day
    cols = cols.reshape(idx.shape[0], 5)

    ## convert the arrays into a pandas DataFrame
    df = pd.DataFrame(cols, index=idx, \
                      columns=['close_price', 'high_price', \
                      'low_price', 'close_price', 'volume'])
    return df


df1 = pd.DataFrame(np.array([
    ['DJ', 0.1],
    ['SP', 0.2],
    ['USDJPY', 0.03]]),
    columns=['Asset', 'Returns'])

df2 = pd.DataFrame(np.array([
    ['USA', 'E', 'DJ'],
    ['USA', 'E', 'SP'],
    ['USA', 'FX', 'USDJPY']]),
    columns=['Country', 'Class', 'Asset'])

df1.merge(df2, on="Asset")

df1.merge(df2, on="Asset").set_index(['Country','Class','Asset'])

import requests

url = 'https://api.github.com/repos/pandas-dev/pandas/issues'

resp = requests.get(url)

resp
<Response [200]>

table = df[['Qu1', 'Qu2', 'Qu3']].apply(lambda x: x.value_counts())
table.rename(index=str)


frame.loc[frame.index[:5], 'a'] = np.nan

# for index, only operation is possible
df.rename(index=str, columns={"A": "a", "B": "c"})
df2['four'].fillna('missing')
df.dropna(axis=0)

df.replace([r'\.', r'(a)'], ['dot', '\1stuff'], regex=True)

s.replace({'jf':'abc'})

using nested dictionary
df.replace({'b': {'b': r''}}, regex=True)

# drop the duplicate
df.drop_duplicates(['net','whole'])
df['net'].duplicated()
df.append(df2, ignore_index=True)
# The most familiar way to visualize a bivariate distribution is a scatterplot, where each observation is shown with point at the x and y values.
# While pivot provides general purpose pivoting of DataFrames with various data types (strings, numerics, etc.), Pandas also provides the pivot_table function for pivoting with aggregation of numeric data.


        A  B    C         D         E          F
0     one  A  foo -1.988198  1.034715 2013-01-01
1     one  B  foo -1.988260 -0.779266 2013-02-01
2     two  C  foo -0.374785 -0.403799 2013-03-01
3   three  A  bar  0.205511 -0.833207 2013-04-01
4     one  B  bar  0.665442  0.230856 2013-05-01
5     one  C  bar -0.775207 -0.694308 2013-06-01
6     two  A  foo -0.883282  0.840954 2013-07-01
7   three  B  foo  0.251806  0.882030 2013-08-01
8     one  C  foo  0.069383 -0.241567 2013-09-01
9     one  A  bar  0.546847 -1.430124 2013-10-01
10    two  B  bar  0.584874  1.696377 2013-11-01
11  three  C  bar -0.658417 -1.071053 2013-12-01
12    one  A  foo -0.557717 -0.369010 2013-01-15
13    one  B  foo -1.419855 -0.580672 2013-02-15
14    two  C  foo -1.219685 -0.615864 2013-03-15
15  three  A  bar -1.164137  0.280715 2013-04-15
16    one  B  bar  1.033467 -0.668083 2013-05-15
17    one  C  bar -0.766489 -1.172752 2013-06-15
18    two  A  foo  0.401780 -1.550060 2013-07-15
19  three  B  foo -1.787132 -0.732978 2013-08-15
20    one  C  foo -0.582600 -0.238915 2013-09-15
21    one  A  bar  0.382952 -0.688353 2013-10-15
22    two  B  bar -0.238757  0.350651 2013-11-15
23  three  C  bar  1.464642  0.275761 2013-12-15

# pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
# 1) this is going to generate a new dataframe
# 2) in this new data frame - 
#     the unique value from 'A' and 'B' will be the new index
#     the unique value from 'C' will be be the new column name
#     the value from column D will be aggregated ( defalue is np.mean )

# pivot() is purely to put unique value as column, pivot_table can do aggregation
# Pivot tables generally offer a batch of added benefits and features that may not be available with crosstabs. 
# rename is to rename the index or columns intead of actual data

# we can use replace from df to do the replacement
df.replace({'\n': '<br>'}, regex=True)

regex_pat = re.compile(r'^.a|dog', flags=re.IGNORECASE)

s3.str.replace(regex_pat, 'XX-XX ')

# str function is used only for index if it is used for Series
# this will drop the rows with the condition

df.drop(df[df.score < 50].index, inplace=True)

# based on index
df.drop(['a', 'd'], axis=0)

#based on column
df.drop(['one'], axis=1)

df['attacker_size'][df['year'] == 298][df['attacker_outcome']== 'win']


#alchedemy


td_engine_prod = create_engine('teradata://gaoyangao:T0021193H@10.89.140.97')

pd.read_sql('select * from bip_vtdb.v0177_data_source_type',td_engine_prod)

pip install sqlalchemy-teradata

from sqlalchemy import create_engine


pandas.to_datetime
Convert argument to datetime.
pandas.to_timedelta
Convert argument to timedelta.
pandas.to_numeric
Convert argument to a numeric type.
numpy.ndarray.astype
Cast a numpy array to a specified type.

dd.length.apply(pd.to_numeric)

dd.length.astype(int,errors='ignore')

def coltype(x):
      ...:     return x, '{} abc'.format(x)

dd['1'],dd['2'] =zip(*dd['physical datatype'].map(coltype)
      ...: )

df.join(df.apply(lambda x: myfunc(x['a'],x['b'],x['c']),axis=1))
Or pd.concat

pd.concat([df, df.apply(lambda x: myfunc(x['a'],x['b'],x['c']),axis=1)], axis=1)
(iris.query('SepalLength > 5')
   ....:      .assign(SepalRatio = lambda x: x.SepalWidth / x.SepalLength,
   ....:              PetalRatio = lambda x: x.PetalWidth / x.PetalLength)
   ....:      .plot(kind='scatter', x='SepalRatio', y='PetalRatio'))

df['Normalized'] = np.where(df['Currency'] == '$', df['Budget'] * 0.78125, df['Budget'])

series.apply(subtract_custom_value,args=(5,))

print("{name:8.3f}".format(name=234.2346))
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))



Randomly sample rows from a DataFrame
Sampling is commonly used in Machine Learning tasks and many others.

# sample 4 rows from df
random_indices = np.random.choice(df.index.values, 4, replace=False)

# iloc retrieves rows by position, but the dataframe is now smaller
# so use loc instead (loc retrieves rows by their numeric indices)
sampled_df = df.loc[random_indices]


Iterate over all rows in a DataFrame
Using for ... in. This is similar to iterating over Python dictionaries (think iteritems() or items()in Python 3):

for index,row in df.iterrows():
    print("{0} has name: {1}".format(index,row["name"]))


Use pd.concat() along the column axis

# original dataframe df is not modified
pd.concat([df,pd.get_dummies(df["state"])],axis=1)



Convert a column to another dtype
Use astype().

print(my_df['my_column'].dtype)
# prints dtype('int32')

my_df['my_column'] = my_df['my_column'].astype('uint8')

print(my_df['my_column'].dtype)



Create an empty Dataframe and append rows
Use append() with ignore_index=True.

# set column names and dtypes
new_df = pd.DataFrame(columns=['col_a','col_b']).astype({'col_a':'float32', 'col_b':'int8'})


# must reassign since the append method does not work in place
new_df = new_df.append({'col_a':5,'col_b':10}, ignore_index=True)
new_df = new_df.append({'col_a':1,'col_b':100}, ignore_index=True)

new_df


# iloc can take a list of index
# g.groups[i] holds all the index under this group
for i in g.groups.keys():
      ...:     print dd['pk'].iloc[g.groups[i]]



dd['physical datatype'].str.split().str.get(2)

s2.str.split('_', expand=True)



df = pd.DataFrame({"a":range(4),"b":range(1,5)})


df[['e','f']] = df.apply( lambda x: divideAndMultiply(x["a
      ...: "],x["b"]) , axis =1)


def divideAndMultiply(x,y):
      ...:     return [x/y, x*y]



tips.groupby('day').agg({'tip': np.mean, 'day': np.size})

#for column operation
x = i[3:4].append(i[4:8]).append(i[4:9])
#for list operation
l[2:4] + l [:10]



import pandas as pd


# Create some Pandas dataframes from some data.
df1 = pd.DataFrame({'Data': [11, 12, 13, 14]})
df2 = pd.DataFrame({'Data': [21, 22, 23, 24]})
df3 = pd.DataFrame({'Data': [31, 32, 33, 34]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_multiple.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
df1.to_excel(writer, sheet_name='Sheet1')
df2.to_excel(writer, sheet_name='Sheet2')
df3.to_excel(writer, sheet_name='Sheet3')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
