def Mex(a):
    co = 0
    ac = a.copy()
    myset = set(ac)
    ac = list(myset)
    ac.sort()
    for i in range(len(ac)):
        if(ac[i]==co):
            pass
        else:
            print(co)
            return co
        co+=1
    print(co)
    return co
Mex([0,0])
