# cook your dish here
def sol(n,arr):
    res = [0]*(n+1)
    for i in range(len(arr)):
        if arr[i]<n+1:
            res[arr[i]] += 1
        
    ans = []
    count = 0
    for i in range(len(res)):
        if res[i]>1:
            ans.append(i)
            count += 1
    
    if len(ans)>0:
        return count,ans
    else:
        return count,ans
    
if __name__ == "__main__":
    t = int(input())
    while t>0:
        n,m,k = input().split()
        n = int(n)
        m = int(m)
        k = int(k)
        arr = list(map(int, input().split()))
        count,ans = sol(n,arr)
        if count == 0:
            print(count)
        else:
            print(count, end = " ")
            for i in ans:
                print(i,end = " ")
            print("")
        t = t-1
else:
    pass