for _ in range(int(input())):
    n = int(input())
    P = list(map(int,input().split()))
    zeros = P.count(0)
    count=0
    Pr=[]
    if n == zeros:
        print(zeros)
    else:
        giv = set(x for x in P if x != 0)
        miss = sorted(set(range(1, n+1)) - giv, reverse=True)
        filled = []
        id = 0
        for x in P:
            if x == 0:
                filled.append(miss[id])
                id += 1
            else:
                filled.append(x)
        i=0
        l, r = -1, -1
        for i in range(n-1):
            if filled[i] > filled[i+1]:
                l = i
                break
        for j in range(n-1, 0, -1):
            if filled[j-1] > filled[j]:
                r = j
        if l == -1:
            ans = 0
        else:
            print(filled)
            print(r,l)
            print((r-l)+1)