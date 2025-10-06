for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    flag=False
    for i in range(n):
        if flag == False:
            for x in range(i+1,n):
                s1 = sum(A[0:i+1])
                s2 = sum(A[i+1:x+1])
                s3 = sum(A[x+1:])
                if ((s1%3==s2%3)and(s2%3==s3%3)and(s1%3==s3%3)) or ((s1%3!=s2%3)and(s2%3!=s3%3)and(s1%3!=s3%3)):
                    #print(s1%3,s2%3,s3%3)
                    print(i+1,end=" ")
                    print(x+1,end="\n")
                    flag = True
                    break
        else:
            break
    if flag == False:
        print(0,end=" ")
        print(0,end="\n")
            