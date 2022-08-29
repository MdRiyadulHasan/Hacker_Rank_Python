def birthdayCakeCandles(arr):
    big = max(arr)
    big_count = arr.count(big)
    return big_count
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int,input().strip().split()))
    total = birthdayCakeCandles(arr)
    print(total)