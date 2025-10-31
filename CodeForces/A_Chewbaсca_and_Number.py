n = str(input())
num = list(n)
ans=[]
if int(num[0])>4 and num[0]!=9:
    ans.append(9-int(num[0]))
else:
    ans.append(int(num[0]))
for i in range(1,len(num)):
    x=num[i]
    if int(x)>4:
        ans.append(9-int(x))
    else:
        ans.append(int(x))
for x in ans:
    print(x,end="")
print()