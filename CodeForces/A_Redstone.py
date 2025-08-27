for _ in range(int(input())):
    n = int(input())
    gears = list(map(int,input().split()))
    ratios = {}
    for i,x in enumerate(gears):
        ratios[x]=ratios.get(x,0)+1
    num = ratios.values()
    maxi = max(num)
    if maxi>=2:
        print("Yes")
    else:
        print("No")