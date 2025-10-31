n,k = map(int,input().split())
L = list(map(int,input().split()))
L.sort()
D=0
for i in range(1,n):
    temp = abs(L[i]-L[i-1])
    D = max(D,temp)
print(float(max(D/2,L[0],abs(k-L[-1]))))