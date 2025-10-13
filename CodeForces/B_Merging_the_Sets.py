from random import getrandbits
RD = getrandbits(31)
for _ in range(int(input())):
    n,m=map(int,input().split())
    li={}
    owner=[-1]*(m+1)
    for i in range(n):
        ar = list(map(int,input().split()))
        del ar[0]
        for j in range(len(ar)):
            li[ar[j]^RD]=li.get(ar[j]^RD,0)+1
            owner[ar[j]]=i
    cnt=[]
    done=False
    for x in range(1,m+1):
        if not li.get(x^RD):
            done=True
            break
        elif li[x^RD]==0:
            done=True
            break
        elif li[x^RD]==1:
            cnt.append(owner[x])
    if done:
        print("NO")
    elif n-len(set(cnt))>=2:
        print("YES")
    else:
        print("NO")