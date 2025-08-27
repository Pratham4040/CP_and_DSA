t = int(input())
for _ in range(t):
    n,s= map(int,input().split())
    nums = list(map(int,input().split()))
    
    if(s == sum(nums)+1 or sum(nums)>s):
        x= nums.count(0)
        y = nums.count(1)
        z= nums.count(2)
        ans1 = [0]*x
        ans2 = [2]*z
        ans3 = [1]*y
        ans = ans1 + ans2 + ans3
        for x in ans:
            print(x,end=" ")
        print("\n",end="")
    else:
        print(-1)
        
