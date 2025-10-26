A=[]
flag=False
n = int(input())
for _ in range(n):
    x= int(input())
    A.append(x)
all_done=[]
for i in range(2**n):
    s = bin(i)
    if(len(s[2:])<n):
        s="0"*(n-len(s[2:]))+s[2:]
    else:
        s=s[2:]
    ans=0
    p=0
    #print(s)
    for x in s:
        if p < n:
            if x =="0":
                ans+=A[p]*(1)
            else:
                ans+=A[p]*(-1)
        p+=1
    #print(ans)
    if ans%360==0:
        flag=True
        break
if flag==True:
    print("YES")
else:
    print("NO")