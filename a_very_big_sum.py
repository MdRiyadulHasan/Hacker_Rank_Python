def aVeryBigsum(arr):
    return sum(arr)
if __name__== '__main__':
    n=int(input().strip())
    arr = list(map(int,input().strip().split()))
    result = aVeryBigsum(arr)
    print(result)