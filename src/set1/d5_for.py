my_list = [('apple', 'orange', 'banana', 'grape'), (1, 2, 3)]

for item in my_list:
    for child in item:
        print(child, end=' ')
else:
    print('遍历结束')