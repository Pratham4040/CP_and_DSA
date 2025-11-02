for _ in range(int(input())):
    n = int(input())
    c=0
    l = list(map(int,input().split()))
    s=[]
    for i in range(1,n+1):
        s.append(l[i-1]-i)
    #print(s)      
    di={}
    for x in s:
        di[x]=di.get(x,0)+1
    #print(di)
    for x in di.keys():
        t = di[x]-1
        c+=(t*(t+1))//2
    print(c)