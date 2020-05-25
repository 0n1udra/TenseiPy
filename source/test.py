test1 = {'one':{'1.1':'ONE'}}
test2 = {'one':{'1.2':'ONETWO'}}
test3 = (*test1, *test2)
print(test3)
