def swapCase(s):
    s=list(s)
    l=len(s)
    for i in range(l):
        if str.islower(s[i]):
            s[i]=str.upper(s[i])
        else:
            s[i] = str.lower(s[i])
    return ''.join(s)

if __name__ == '__main__':
    s=input()
    result = swapCase(s)
    print(result)