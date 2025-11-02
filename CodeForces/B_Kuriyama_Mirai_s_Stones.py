n = int(input())
l = list(map(int,input().split()))
so = l.copy()
so.sort()
sums=[]
sums1=[]
sums.append(l[0])
for i in range(1,n):
    sums.append(l[i]+sums[i-1])
sums1.append(so[0])
for i in range(1,n):
    sums1.append(so[i]+sums1[i-1])
q=int(input())
for _ in range(q):
    l2 = list(map(int,input().split()))
    ty = l2.pop(0)
    if (ty == 1):
        if l2[0] == 1:
            print(sums[l2[-1]-1])
        else:
            print(sums[max(l2[-1]-1,0)]-sums[max(l2[0]-2,0)])
    else:
        if l2[0] == 1:
            print(sums1[l2[-1]-1])
        else:
            print(sums1[max(l2[-1]-1,0)]-sums1[max(l2[0]-2,0)])