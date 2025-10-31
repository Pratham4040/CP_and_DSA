for _ in range(int(input())):
    n,k = map(int,input().split())
    if k == 1 :
        if n %2 != 0:
            print("YES")
        else:
            print("NO")
    else:
        if n % 2 == 0 and k%2 ==0:
            if n >= k*k:
                print("YES")
            else:
                print("NO")
        elif n % 2 != 0 and k%2 !=0:
            if n >= k*k:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")