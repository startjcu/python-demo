# python中返回多个值，用逗号分隔
def demages(skill1, skill2):
    damage1 = skill1*3
    damage2 = skill2*2+10
    return damage1, damage2


print(demages(2, 3))

# 序列解包
# 用多个变量存储函数返回的多个值
skill1_damage, skill2_damage = demages(2, 3)
print(skill1_damage, skill2_damage)

d = 1, 2, 3
print(type(d))
