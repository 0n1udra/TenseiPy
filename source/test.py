
def gen1(y=False):
    for i in range(10):
        yield i
        if i == 5:
            break


x = [i for i in gen1()]
print(x)
