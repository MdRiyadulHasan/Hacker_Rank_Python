def change(c):
    if str.islower(c):
        return str.upper(c)
    else:
        return str.lower(c)

def swapCase(s):
    return ''.join(map(change,s))

if __name__ == '__main__':
    s=input()
    result = swapCase(s)
    print(result)