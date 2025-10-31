import math
def prime(i, primes):
    for prime in primes:
        if not (i == prime or i % prime):
            return False
    primes.add(i)
    return i
# def historic(n):
#     primes = set([2])
#     i, p = 2, 0
#     while True:
#         if prime(i, primes):
#             if i > n:
#                 return primes
#         i += 1
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    l.sort()
    sm = l[0]
    primes = set([2])
    i, p = 2, 0
    flag=True
    ans=-1
    while True:
        if flag == False:
            break
        for x in l:
            if math.gcd(x,i)==1:
                ans=i
                flag=False
                break
        i += 1        
    print(ans)
    