for _ in range(int(input())):
    n=int(input())
    d = list(map(int,input().split()))
    d.sort()
    c=0
    di = {}
    for x in d:
        di[x]=di.get(x,0)+1
    print(di)
    for i in di.keys():
        if i<=di[i]:
            c+=di[i]//i+(i-1)
    print(c)