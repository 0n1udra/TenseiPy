
class test():
    def __init__(self):
        self.testy = 'nope'
        self.testvar = self.testy

class test2(test):
    def __init__(self):
        test.__init__(self)
        self.testy = 'hi'
        self.testVar = super().__init__().testVar



y = test2()
print(y.testvar)
print(y.testy)
