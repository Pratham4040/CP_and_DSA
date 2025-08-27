from fractions import Fraction

for _ in range(int(input())):
    a,b,k=map(int,input().split())
    t=a
    a=max([a,b])
    b=min([t,b])
    f=Fraction(a,b)
    if f.denominator<=k and f.numerator<=k:
        print(1)
    else:
        print(2)