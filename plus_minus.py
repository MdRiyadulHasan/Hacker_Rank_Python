def plus_minus(arr):
    p=0
    ng =0
    z = 0
    for i in range(n):
        if(arr[i]>0):
            p=p+1
        elif(arr[i]<0):
            ng=ng+1
        else:
            z=z+1
    print(p/n)
    print(ng/n)
    print(z/n)


if __name__ == '__main__':
    n =int(input().strip())
    arr = list(map(int, input().strip().split()))
    plus_minus(arr)