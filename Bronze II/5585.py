int_num = 1000 - int(input())
res_count=0
jandon = [500, 100, 50, 10, 5, 1]

for i in jandon:
    if int_num>=i:
        moc, int_num = divmod(int_num, i)
        res_count += moc

print(res_count)