class Student(object):
    def __init__(self, id, name, marks):
        self.id = id
        self.name = name
        self.marks = marks

    def __str__(self):
        return '%s has marks %s' % (self.name, self.marks)
