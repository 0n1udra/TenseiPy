lest = [['1', '2'], ['3', '4']]

lest = [i for j in lest for i in j]
x = '3'
if x in lest:
    print("HI")
