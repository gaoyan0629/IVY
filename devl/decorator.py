import sys
try:
    # Python 2
    import __builtin__ as builtins
except ImportError:
    # Python 3
    import builtins

def property(function):
    keys = 'fget', 'fset', 'fdel'
    func_locals = {'doc':function.__doc__}
    def probe_func(frame, event, arg):
        print 'frame',frame
        print 'event',event
        print 'arg',arg
        if event == 'return':
            locals = frame.f_locals
            func_locals.update(dict((k, locals.get(k)) for k in keys))
            sys.settrace(None)
        return probe_func
    sys.settrace(probe_func)
    function()
    return builtins.property(**func_locals)

#====== Example ==========================

from math import radians, degrees, pi

class Angle(object):
    def __init__(self, rad):
        self._rad = rad

    @property
    def rad():
        '''The angle in radians'''
        def fget(self):
            return self._rad
        def fset(self, angle):
            if isinstance(angle, Angle):
                angle = angle.rad
            self._rad = float(angle)

    @property
    def deg():
        '''The angle in degrees'''
        def fget(self):
            return degrees(self._rad)
        def fset(self, angle):
            if isinstance(angle, Angle):
                angle = angle.deg
            self._rad = radians(angle)
