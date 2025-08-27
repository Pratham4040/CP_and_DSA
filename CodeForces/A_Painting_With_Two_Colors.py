for _ in range(int(input())):
    n,a,b = map(int,input().split())
    if b>a:
        diff = n-b
        if diff %2==0:
            print("Yes")
        else:
            print("No")
    else:
        diff1 = n-a
        diff2 = a-b
        if diff1%2==0 and diff2%2==0:
            print("Yes")
        else:
            print("No")