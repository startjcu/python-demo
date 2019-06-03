def divide(x, y):
    return x/y


# 使用必须参数
print(divide(2, 5))
# 使用关键字参数
print(divide(y=2, x=5))


def add(x, y=4, z=0):
    print(x+y-z)


# 默认参数
add(4)
add(3, 2)
# 默认参数和关键字参数结合使用
add(3, z=1)


def doSum(*param):
    sum = 0
    for i in param:
        sum += i
    print('所有参数的和为: {}'.format(sum))


# 可变参数
doSum(1, 2, 3, 4)


def city_temp(**param):
    for key, value in param.items():
        print('{} : {}'.format(key, value))


city_temp(bj='32c', xm='25c')
