n,m,k = map(int,input().split())
l=[]
for _ in range(m+1):
    x = int(input())
    #b=bin(x)
    l.append(x)
#print(l)
cnt=0
main = l[-1]
for i in range(m):
    xor = l[i]^main
    c = bin(xor)[2:].count("1")
    if c <=k:
        cnt+=1
print(cnt)