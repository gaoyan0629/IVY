grouped = df.groupby(cols_to_consider)
index = [gp_keys[0] for gp_keys in grouped.groups.values()]
unique_df = df.reindex(index)


class Polygon(object):
    def __init__(self, id):
        self.id = id
    def __len__(self):
        return len(id) + 20


class Rectangle(Polygon):
    def __init__(self, id, width, height):
        super(self.__class__, self).__init__(id)
        self.shape = (width, height)


class Square(Rectangle):
    pass



su = itertools.product(n,suit)
choice.sample(frac=0.5,replace=True)
choice.sample(n=10,replace=True)

p = itertools.permutations(deck,13)

frame.b=frame.a.str.replace(r'(\w+)(?=/)(.*)',lambda x: x.group(0))

