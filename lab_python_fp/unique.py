class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = []
        if 'ignore_case' in kwargs.keys() and kwargs['ignore_case']:
            self.items = list(set(map(lambda x: x.lower() if type(x) == str else x, items)))
        else:
            self.items = list(set(items))

        self.start = 0
        self.stop = len(self.items)
        self.position = -1


    def __next__(self):
        self.position += 1
        if self.position < self.stop:
            return self.items[self.position]
        else:
            return ''

    def __iter__(self):
        return self
