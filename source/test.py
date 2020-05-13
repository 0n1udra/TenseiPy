class test:
    def __init__(self):
        print("Test init")

class subTest(test):
    def __init__(self):
        test.__init__(self)
        print("Test Sub")

x = subTest()
