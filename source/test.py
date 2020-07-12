class Test:
    cVar = 'hi'
    def __init__(self):
        print(self.cVar)
        pass

    def printVar(self):
        print('Test:', self.cVar)

class Tx(Test):
    def __init__(self):
        print("NEW")

    @classmethod
    def new(cls):
        cls.cVar = 'bye'


x = Tx()
x.new()
x.printVar()
y = Tx()
y.printVar()




