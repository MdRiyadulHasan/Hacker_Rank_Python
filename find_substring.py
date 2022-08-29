def count_substring(string, sub_string):
    l=len(sub_string)
    length = len(string)
    c=0
    for i in range(length):
        if(string[i:i+l]==sub_string):
            c=c+1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)