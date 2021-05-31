def sol(x,m,d):
    res = x*m
    return min(res,x+d)
    
if __name__ == "__main__":
    t = int(input())
    while t>0:
        x,m,d = [int(x) for x in input().split()]
        print(sol(x,m,d))
        t = t-1
else:
    pass
