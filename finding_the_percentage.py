if __name__ =='__main__':
    n=int(input())
    student={}
    for _ in range(n):
        name,*line=input().split()
        marks=list(map(float,line))
        student[name]=marks
    query_name=input()
    total_marks=student[query_name]
    total_marks=sum(total_marks)
    print(format(total_marks/3,'.2f'))
    