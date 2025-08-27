import math
t = int(input())
for _ in range(t):
    n = int(input())
    # x = math.log(n,3)
    # cost1 = int(3**(x+1)+x*(3**(x-1)))
    # tim = n%3
    # rim = int(n//3)
    # cost2 = tim*10 + rim*3
    # cost = min(cost1,cost2)
    # print(cost1,cost2)
    i=1
    parts = []
    count =0 
    if n >=3:
        while 3**i<=n:
            parts.append(3**i)
            count +=1
            i+=1
        maxi = max(parts)
        count =0 
        i=1
        while maxi*i <= n:
            count+=1
            i+=1
        rem = n - maxi*count
        x = math.log(maxi,3)
        cost_maxi = int(3**(x+1)+x*(3**(x-1)))
        if rem == 0:
            rem_cost =0
        else:
            x = math.log(rem,3)
            rem_cost = int(3**(x+1)+x*(3**(x-1)))
        print(rem_cost+cost_maxi)
    else:
        x = math.log(n,3)
        cost1 = int(3**(x+1)+x*(3**(x-1)))
        print(cost1)