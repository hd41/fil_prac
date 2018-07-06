dict = {'100':0, '50':0, '25':0}

def check(bal):
    print(dict)
    if bal == 75:
        if dict['50']==0:
            return False
        else:
            dict['50']-=1
            return True
    elif bal == 25:
        if dict['25']==0:
            return False
        else:
            dict['25']-=1
            return True
    else:
        return True

def tickets(people):

    for i in people:
        if check(i-25):
            pass
        else:
            print(people)
            return "NO"
        dict[str(i)]= dict[str(i)]+1
    return "YES"

print(tickets([25,100]))
