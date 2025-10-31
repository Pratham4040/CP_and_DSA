for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    e=0
    o=0
    for x in l:
        if x % 2 == 0:
            e+=1
        else:
            o+=1
    if e == 0 or o==0:
        for x in l:
            print(x,end=" ")
        print()
    else:
        l.sort()
        for x in l:
            print(x,end=" ")
        print()