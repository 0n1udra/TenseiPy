class me:
    x = 'hello'
    def __init__(self):
        print('ok', self.x)

def foo():
    xin = me()
    xin.x = 'bye'
    class barr:
        class bar:
            def __init__(self):
                print(foo.xin.x)

        bar()
    barr()
def boo():
    class barr:
        xin = me()
        class bar:
            def __init__(self):
                print(xin.x)

        bar()
    barr()

foo()
boo()
