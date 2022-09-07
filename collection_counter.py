from collections import Counter
if __name__ == '__main__':
    n=int(input().strip())
    s=list(map(int,input().strip().split()))
    s=Counter(s)
    t=int(input())
    for i in range(t):
        list_=list(input().strip().split())
        size=int(list_[0])
        price=int(list_[1])
        if size in s.keys() and s[size]!=0:
            sum=sum+price
        s[size]=s[size]-1
    print(sum)
        