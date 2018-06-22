from functools import update_wrapper
class docstring_wrapper(object):
    """
    decorator to wrap a function,
    provide a dynamically evaluated doc-string

    Parameters
    ----------
    func : callable
    creator : callable
        return the doc-string
    default : str, optional
        return this doc-string on error
    """
    _attrs = ['__module__', '__name__',

              '__qualname__', '__annotations__']

    def __init__(self, func, creator, default=None):
        self.func = func
        self.creator = creator
        self.default = default
        update_wrapper(
            self, func, [attr for attr in self._attrs
                         if hasattr(func, attr)])

    def __get__(self, instance, cls=None):

        # we are called with a class
        if instance is None:
            return self

        # we want to return the actual passed instance
        return types.MethodType(self, instance)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    @property
    def __doc__(self):
        try:
            return self.creator()
        except Exception as exc:
            msg = self.default or str(exc)
            return msg
    def __doc__(self):
        try:
            return self.creator()
        except Exception as exc:
            msg = self.default or str(exc)
            return msg


@docstring_wrapper(type,type)
def abc():
    print 'hel'
