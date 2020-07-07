class Test:
    testVar = 'testy var'
    def __init__(self):
        self.testVart  = 'init'


    def printData(self):
        print(self.data)





print(Test.testVar)
Test.testVar = 'hi'
print(Test().testVart)
t = Test()
x = Test()

print(t.testVar)
print(x.testVar)
