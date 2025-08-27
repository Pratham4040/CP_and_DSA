t = int(input())
for _ in range(t):
    n = int(input())
    first = []
    last = []    
    for _ in range(n):
        a,b,c,d = map(int,input().split())
        first.append((a,b))
        last.append((c,d))
    diff = []
    if n == 1:
        print(0)
        continue
    for i in range(n):
        a=first[i][0]
        b=first[i][1]
        c=last[i][0]
        d=last[i][1]
        # if(ac>=0 and bd<0):
        #     diff.append(abs(bd)*(a+1))   
        # elif(ac<0 and bd<0):
        #     diff.append(abs(ac))
        #     diff.append((abs(bd))*(c+1))
            
        # elif(ac<0 and bd>=0):
        #     diff.append(abs(ac))
        # else:
        #     pass
        if(b>d):
            diff.append(b-d+a)
        elif(a>c):
            diff.append(a-c)       
    print(sum(diff))        


