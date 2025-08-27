def solve(ind,health,cost):
    if ind-1>=0:
        cost = health[ind-1]
        
    else:
        cost = maxi
for _ in range(int(input())):
    n = int(input())
    health = list(map(int,input().split()))
    maxi = max(health)
    ind = health.index(maxi)
    cost = 0
    solve(ind,health,cost)