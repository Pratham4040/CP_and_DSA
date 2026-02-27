def factor(n):
    factors=[]
    for i in range(2,int(n**0.5)+1):
        while(n%i==0):
            factors.append(i)
            n=n//i
    if n>1:
        factors.append(n)
    return factors
for _ in range(int(input())):
    n = int(input())
    fact = factor(n)
    # print(fact)
    if len(fact)==3:
        if len(set(fact))==3:
            print("YES")
            for x in fact:
                print(x,end=" ")
            print()
        else:
            print("NO")
    elif len(fact)<3:
        print("NO")
    else:
        ans=[]
        ans.append(fact[0])
        i=1
        cur=1
        while( i < len(fact)):
            if cur == 2:
                x=1
                for p in range(i,len(fact)):
                    x*=fact[p]
                ans.append(x)
                break
            if fact[i-1]!=fact[i]:
                ans.append(fact[i])
                i+=1
                cur+=1
            elif fact[i-1]==fact[i]:
                ans.append(fact[i]*fact[i+1])
                i+=2
                cur+=1
        if len(set(ans))==3:
            print("YES")
            for x in ans:
                print(x,end=" ")
            print()
        else:
            print("NO")
