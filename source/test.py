class Test:
    def __init__(self):
        print("STASRT")
        fun(self)

    def testClassFunc(self):
        print("HI")

    def _testFunc(self):
        print("BYE")

    class Hi:
        def ok():
            pass

print(dir(Test))
