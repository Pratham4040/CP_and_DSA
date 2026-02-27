n,m = map(int,input().split())
maxi = n - m +1
ansm = ((maxi*(maxi-1))//2)
mini = n//m 
ansmin = (mini*(mini-1)//2)
ansmin*=m
#print(ansmin)
#print(((n%m)*(n//m)))
print((ansmin+((n%m)*(n//m))),end=" ")
print(ansm,end=" ")
