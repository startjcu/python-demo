# i, j = 1, 1
i = j = 1
while i <= 9:
    # 格式化输出format以及不换行打印end
    print('{}*{}={}\t'.format(j, i, i*j), end='')
    j += 1
    if j > i:
        print()
        i += 1
        j = 1
else:
    print('打印完毕')
