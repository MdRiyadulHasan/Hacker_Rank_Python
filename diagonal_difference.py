def diagonal_difference(arr):
    sum_a = 0
    sum_b = 0
    
    for i in range(n):
        sum_a = sum_a + arr[i][i]  # diagonal difference left to right
        sum_b = sum_b+arr[i][n-i-1] # diagonal difference right to left
    
    difference = abs(sum_a-sum_b)
    return difference

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().strip().split())))
        
    result = diagonal_difference(arr)
    print(result)