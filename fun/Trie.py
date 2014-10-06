__author__ = 'leon'
class trie:
    def __init__(self):
        self.path = {}
        self.key = None

    def __insert__(self, key, value):
        head = key[0]
        if head in self.path:
            node = 