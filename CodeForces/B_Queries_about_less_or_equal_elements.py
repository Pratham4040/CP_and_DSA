from bisect import bisect_right
n,m = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
l2=list(map(int,input().split()))
for x in l2:
    pos = bisect_right(l,x)
    print(pos,end=" ")
