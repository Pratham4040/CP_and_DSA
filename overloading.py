from multipledispatch import dispatch as dp
@dp(int,int)
def add(a,b):
    print(a+b)
@dp(int,int,int)
def sub(a,b,c):
    print(a-b-c)
def mut(type,*args):
    if(type == 'int'):
        for x in args:
            ans = ans*x
            print(ans)
           
def div(a=None,b=None):
    if a==None:
        print("neumarator cannot be null") 
    elif b==None:
        print("denominator cannot be null")      
    else:
        print(a/b)
add(3,5)
sub(5,3,5)
mut(4,5)
div(7)
div(4,6)
