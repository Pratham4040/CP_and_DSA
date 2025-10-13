k = int(input())
di={}
for i in range(k):
    a,x = map(str,input().split())
    di[i]=di.get(a,[int(x),a])
print(di)

