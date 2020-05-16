
class test():
    def __init__(self):
        self.testvar = 'hello'

class test2(test):
    def __init__(self):
        test.__init__(self)



y = test2()
print(y.testvar)
