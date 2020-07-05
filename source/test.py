class Test:
    def __init__(self):
        print("STASRT")

    def testClassFunc(self):
        print("HI")

    def _testFunc(self):
        print("BYE")

    class Hi:
        def ok():
            pass

li = [1, 2, 5, 6]
print(*[i for i in li])
