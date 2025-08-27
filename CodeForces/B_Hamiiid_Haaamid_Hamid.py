t = int(input())
for _ in range(t):
    n,x= map(int,input().split())
    maze = str(input())
    indx= x-1
    maze1 = list(maze)
    count=0
    count2=0
    maze1[indx+1]='#'
    print(maze1)
    for i in range(indx,-1,-1):
        if maze1[i]=='#':
            count+=indx-i
    for i in range(indx,n-1):
        if maze1[i]=='#':
            count2+=n-indx
    ans1 = min(count,count2)
    print(ans1)
    maze1 = list(maze)
    count=0
    count2=0
    maze1[indx-1]='#'
    print(maze1)
    for i in range(indx,-1,-1):
        if maze1[i]=='#':
            count+=indx
    for i in range(indx,n-1):
        if maze1[i]=='#':
            count2+=n-indx+1
    ans2 = min(count,count2)
    print(ans2)
    anns = max(ans1,ans2)
    print(anns+1)