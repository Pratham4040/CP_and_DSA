p,m = map(int,input().split())
A = list(map(int,input().split()))
n=[]
n.append(1)
s=set()
s.add(A[-1])
for i in range(2,p+1):
    s.add(A[-i])
    n.append(len(s))
#print(n)
for _ in range(m):
    x = int(input())
    print(n[-x])