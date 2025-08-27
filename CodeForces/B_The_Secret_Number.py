t = int(input())
for _ in range(t):
    n = int(input())
    nu = str(n)
    ans = []
    leng_2 = len(nu)/2
    if set(nu)!=1:
        print(0)
    elif(len(nu)%2 !=0):
        print(0)
    else:
        nuw =""
        ans.append(nu[:int(len(nu/2))])
        for i in range(len(nu)-1):
            nuw +=nu[0]
            nuw +='0'
        ans.append(nuw)
        
