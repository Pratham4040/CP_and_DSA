n = int(input())
l = list(map(int,input().split()))
l2=[]
l2 = l.copy()
l2.sort()
le=-1
r=-1
#print(l,l2)
for i in range(1,n+1):
    if l[i-1]!=l2[i-1]:
        if le == -1:
            le=i
        else:
            r = i
#print(le,r)
if le == -1 and r == -1:
    print("yes")
    print(1,end=" ")
    print(1,end=" ")

else:
    test=[]
    for i in range(n):
        if i>=le-1 and i <=r-1:
            test.append(l[r-1-i+le-1])
        else:
            test.append(l[i])
    #print(test)
    flag=True
    for i in range(1,n+1):
        if test[i-1]!=l2[i-1]:
            flag=False
    if flag==False:
        print("no")
    else:
        print("yes")
        print(le,end=" ")
        print(r,end=" ")