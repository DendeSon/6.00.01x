#Problem 7
   
class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        self.aDict = {}
        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        self.k = k
        self.v = v
        if self.k not in self.aDict:
            self.aDict[self.k] = self.v
        else:
            self.aDict[self.k] = self.v        
        
    def getval(self, k):
        """ k, immutable object  """
        if k in self.aDict.keys():
            return self.aDict[k]
        else:
            raise KeyError
        
    def delete(self, k):
        """ k, immutable object """   
        if k in self.aDict.keys():
            del self.aDict[k]
        else:
            raise KeyError