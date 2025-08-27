for _ in range(int(input())):
    n = int(input())
    num = list(map(int,input().split()))
    cost=0
    if num[0]>num[1]:
            cost+=abs(num[0]-num[1])
            num[0]= num[1]
    i=2
    while i < n:
        diff = abs(num[i-1]-num[i-2])
        if i+1 <n:
             diff = min(diff,num[i+1])
        if num[i]>diff:
            cost +=num[i]-diff
            num[i]=diff
        i+=2
    print(cost)