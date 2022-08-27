def compareTriplets(a,b):
    l=len(a)
    c=int(0) # counter for a 
    d=int(0) # counter for b
    for i in range(l):
        if (a[i]>b[i]):
            c=c+1
        elif (b[i]>a[i]):
            d=d+1  
    return c,d
if __name__ == '__main__':
    a=list(map(int,input().strip().split()))
    b=list(map(int, input().strip().split()))
    ans_a, ans_b = compareTriplets(a,b)
    print(ans_a, ans_b)