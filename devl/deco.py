def p_decorate(func):
   def func_wrapper(*args, **kwargs):
       print "Decorator is started"
       return "<p>{0}</p>".format(func(*args, **kwargs))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"
# added from mac
    @p_decorate
    @property
    def get_fullname(self):
        return self.name+" "+self.family
   # added this correctly
