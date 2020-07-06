class Test:
    def __init__(self):
        print("ok")
        self.data = 'hi'


    def printData(self):
        print(self.data)




class One(Test):
    def __init__(self):
        self.data = 'ok'


one = One()
one.printData()
