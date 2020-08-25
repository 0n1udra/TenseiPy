x = [1,2,3]

def test():
    for i in x:
        yield i

for i in test():
    if i == 2:
        del i

print(x)
