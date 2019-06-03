from d2_Student import Student

# 创建对象，类的实例化
stu = Student('xiaolin', 22)
# 通过对象调用方法
stu.print_file()
# 属性字典
print(stu.__dict__)
# 访问类变量
print(Student.age)
print(stu.__class__)
# 间接读取私有变量
print(stu.__class__._Student__name)
# 调用类方法
Student.cls_method()
# 静态方法的调用
stu.stc_method()
Student.stc_method()
