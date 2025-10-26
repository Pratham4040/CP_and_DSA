n = int(input())
di = {}
flag=False
for i in range(n):
    a,b = map(int,input().split())
    di[a]=di.get(a,b)
s_k = list(di.keys())
s_k.sort()
for i in range(1,len(s_k)):
    if di[s_k[i-1]]>di[s_k[i]]:
        flag=True
        break
if flag:
    print("Happy Alex")
else:
    print("Poor Alex")