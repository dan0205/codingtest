N=int(input())
student_list = list(map(int,input().split()))
B, C = map(int,input().split())

res_count=N

for num in student_list:
    student_num = num - B
    if student_num == 0:
        continue
    else:
        moc, namuji = divmod(student_num, C)
        if namuji==0:
            res_count+=moc
        else:
            res_count+=moc+1

print(res_count)



