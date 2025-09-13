import math
for _ in range(int(input())):
    n= int(input())
    A = list(map(int,input().split()))
    e=[]
    o=[]
    for i in range(n):
        if A[i]%2==0:
            e.append(A[i])
        else:
            o.append(A[i])
    o.sort(reverse=True)
    if len(o)!=0:
        sumi = sum(e)
        no = math.ceil(len(o)/2)
        for i in range(no):
            sumi+=o[i]
        print(sumi)   
    else:
        print(0)
