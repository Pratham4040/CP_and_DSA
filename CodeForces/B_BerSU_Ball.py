n = int(input())
l=list(map(int,input().split()))
m = int(input())
l2=list(map(int,input().split()))
l.sort()
l2.sort()
cnt=0
if n < m:
    for i in range(n):
        for j in range(m):
            if l[i]==l2[j] or l[i]==l2[j]+1 or l[i]==l2[j]-1:
                cnt+=1
                l2[j]=-1
                break
else:
    for i in range(m):
        for j in range(n):
            if l2[i]==l[j] or l2[i]==l[j]+1 or l2[i]==l[j]-1:
                cnt+=1
                l[j]=-1
                break
print(cnt)
