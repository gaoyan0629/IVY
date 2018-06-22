class party(object):
    def __init__(self, cust):
        self._cust = cust

    @property
    def cust(self):
        return self._cust

    @cust.setter
    def cust(self, value):
        self._cust = value
