
def simpleArraySum(ar):
    return sum(ar)
if __name__ == '__main__':
    n= int(input().strip()) # number of elements in the array
    ar=list(map(int,input().strip().split())) # the elements of the array
    result = simpleArraySum(ar)
    print(result)