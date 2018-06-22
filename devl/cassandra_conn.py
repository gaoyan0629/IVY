from cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy
import pandas as pd
import numpy as np
import csv

cluster = Cluster(
    ['127.0.0.1'],
    load_balancing_policy=DCAwareRoundRobinPolicy(local_dc='US_EAST'),
    port=9042)
cluster = Cluster()
session = cluster.connect("mydb")
rows = session.execute('SELECT id, year, title from books')
# df = pd.read_csv('books.csv')
# print(df)
with open('books.csv', 'rb') as csvfile:
    data = csv.reader(csvfile, delimiter=';')
    # for i in data:
    #     print i
    for i in data:
        mysql = "insert into books(id,title,year) \
                values({},'{}','{}');".format(i[0], i[1], i[2])

        print mysql
        rows = session.execute(mysql)
    rows = session.execute('SELECT id, year, title from books')

rows = session.execute('SELECT key1, map1, list1, set1 from example;')

print type(rows)
print dir(rows)

for i in rows:
    print i.key1
    print "the type of map1 is {}".format(type(i.map1))
    print i.map1
    for j in i.map1:
        print j
    print i.list1
    print i.set1



