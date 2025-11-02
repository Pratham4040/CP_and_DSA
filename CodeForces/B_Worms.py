import bisect
n = int(input())
l = list(map(int,input().split()))
p = int(input())
w = list(map(int,input().split()))
l2=[]
l2.append(l[0])
for i in range(1,n):
    l2.append(l[i]+l2[i-1])
for x in w:
    print((bisect.bisect_left(l2,x))+1)