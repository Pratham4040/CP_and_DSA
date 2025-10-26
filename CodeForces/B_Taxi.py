import math
from random import getrandbits
RD = getrandbits(32)
n = int(input())
G = list(map(int,input().split()))
di={}
for x in G:
    di[x^RD]=di.get(x^RD,0)+1
taxi=di.get(4^RD,0)
m=min(di.get(3^RD,0),di.get(1^RD,0))
#print(m)
taxi+=m
di[3^RD]=di.get(3^RD,0)-m
di[1^RD]=di.get(1^RD,0)-m
taxi+=di.get(3^RD,0)
di[3^RD]=di.get(3^RD,0)-di.get(3^RD,0)
taxi+=di.get(2^RD,0)//2
#print(taxi)
rem=(di.get(2^RD,0)%2)*2
#print(rem)
rem+=di.get(1^RD,0)
#print(rem)
if rem>0:
    taxi+=(rem+3) // 4
print(taxi)