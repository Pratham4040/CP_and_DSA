from random import getrandbits
RD = getrandbits(32)
n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
dic ={}
bic={}
for i in range(n):
    dic[A[i]^RD]=dic.get(A[i]^RD,0)+1
    if i<len(B):
        bic[B[i]^RD]=bic.get(B[i]^RD,0)+1
#print(dic)
for x in B:
    dic[x^RD]=dic.get(x^RD)-1
    if dic[x^RD]==0:
        dic.pop(x^RD)
for x in C:
    bic[x^RD]=bic.get(x^RD)-1
    if bic[x^RD]==0:
        bic.pop(x^RD)
print((list(dic.keys())[0])^RD)
print((list(bic.keys())[0])^RD)
# for x in B:
#     if dic[x]>0