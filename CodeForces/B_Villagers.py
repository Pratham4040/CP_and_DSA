for _ in range(int(input())):
    n = int(input())
    greed = list(map(int,input().split()))
    greed.sort(reverse=True)
    cost=0
    for i in range(0,n-1,2):
        cost += max(greed[i],greed[i+1])
    if n%2 == 0:
        print(cost)
    else:
        print(cost+greed[-1]) 
