for _ in range(int(input())):
    n = int(input())
    s = str(input())
    ind0 = [index for index, char in enumerate(s) if char == '0']
    ind1 = [index for index, char in enumerate(s) if char == '1']
    c0 = len(ind0)
    c1 = len(ind1)
    if c0%2!=0:
        print(c0)
        for x in ind0:
            print(x+1,end=" ")
        print()
    elif c1%2==0:
        print(c1)
        if c1!=0:
            for x in ind1:
                print(x+1,end=" ")
            print()
    else:
        print(-1)