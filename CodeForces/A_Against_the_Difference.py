for _ in range(int(input())):
    n = int(input())
    a  = list(map(int,input().split()))
    di = {}
    for x in a:
        di[x]=di.get(x,0)+1
    div={}
    for x in di:
        div[x]=div.get(x,int(di[x]//x))
    so=sorted(div.keys(),reverse=True)
    for x in so:
        