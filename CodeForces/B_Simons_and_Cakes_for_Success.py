import math
for _ in range(int(input())):
    n = int(input())
    ans = 1
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            ans *=i
        while n %i == 0:
            n //=i
    ans*=n
    print(ans)