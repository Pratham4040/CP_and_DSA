t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    if 0 in nums:
        print("NO")
    else:
        myset = set(nums)
        number = list(myset)
        number = [i for i in number if i != -1]
        if len(number)==1 or len(number)==0:
            print("YES")
        else:
            print("NO")
