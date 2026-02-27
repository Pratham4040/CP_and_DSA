n = int(input())
l = list(map(int,input().split()))
if len(set(l))==1:
    print(0,end=" ")
    print((n*(n-1)//2),end=" ")   
else:
    l.sort()
    m = l.count(l[0])
    le=l.count(l[-1]) 
    print(l[-1]-l[0],end=" ")
    print(m*le,end=" ")