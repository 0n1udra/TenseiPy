def testy():
    print("testy")

x = {
        'dict1':[testy],
        'dict2':[]
        }

x['dict1'].index(testy)()
