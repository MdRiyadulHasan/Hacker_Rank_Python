if __name__ =='__main__':
    N=int(input())
    res=[]
    grade=[]
    for i in range(N):
        name=input()
        marks=float(input())
        res.append([name,marks])
        grade.append(marks)
    grade=sorted(set(grade))
    m=grade[1]
    name=[]
    for val in res:
        if m==val[1]:
            name.append(val[0])
    name.sort()
    for i in name:
        print(i)
        