from d1_People import People

# 定义类


class Student(People):
    # 将成员变私有
    __name = 'star'
    age = 18

    # 实例方法，self指代当前对象
    def print_file(self):
        print('name: ' + self.__name)
        print('age: ' + str(self.age))

    # 构造函数
    def __init__(self, name, age):
        super(Student, self).__init__()
        self.__name = name
        self.age = age
        print('this is constructor')

    # 类方法，cls指代当前类
    @classmethod
    def cls_method(cls):
        print('this is class method')

    # 静态方法，可以不传任何参数
    @staticmethod
    def stc_method():
        print(Student.__name)
        print('this is static method')
