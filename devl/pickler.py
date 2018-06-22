import pickle
from dict import *
a =  Person(60)
a.age = 90

with open("save.p", "wb") as f:
    myStuff = {'gao':'yan'}
    myStuff = a
    pickle.dump(myStuff, f)
    f.close()

try:
    with open("save.p", "rb") as f:
        myStuff = pickle.load(f)
        print myStuff.age
except:
    myStuff = defaultdict(dict)
