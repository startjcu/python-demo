# 指定其他模块通过*能引入的变量和函数
__all__ = ['a', 'c']
a = 1
b = 2
c = 3
print('name: '+__name__)
print('package: '+(__package__ or '当前模块不属于任何包'))
print('doc: ' + (__doc__ or '当前模块没有文档注释'))
print('file: '+__file__)
