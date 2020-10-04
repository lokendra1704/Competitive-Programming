import sys
def fun(n,k,x,y):
    if n==1 or k==1 or x==y:
        return 'YES'
    else:
        t = x
        while True:
            x = (x+k)%n
            if x==y:
                return 'YES'
            elif x==t:
                return 'NO'
            else:
                continue
t = int(sys.stdin.readline())
for k in range(t):
    N,K,X,Y = map(int,sys.stdin.readline().split())
    print(fun(N,K,X,Y))