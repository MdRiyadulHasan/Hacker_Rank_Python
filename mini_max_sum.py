def minMaxSum(arr):
    min_sum=0
    max_sum=0
    min_sum = sum(arr)-max(arr)
    max_sum= sum(arr)-min(arr)
    return min_sum,max_sum

if __name__=='__main__':
    arr = list(map(int,input().strip().split()))
    sum_min, sum_max=minMaxSum(arr)
    print(sum_min, sum_max)