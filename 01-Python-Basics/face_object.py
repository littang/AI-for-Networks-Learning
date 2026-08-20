#类定义
'''
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
'''
#类对象
class MyClass:
    i = 114514
    def f(self):
        return 'aloha'

#实例化类,并访问
x = MyClass()
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())
#以上创建了一个新的类实例并将该对象赋给局部变量 x，x 为空的对象。

def __init__(self):
    self.data = []
#类定义了 __init__() 方法，类的实例化操作会自动调用 __init__() 方法。如实例化类 MyClass，对应的 __init__() 方法就会被调用:

#当然， __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)   # 输出结果：3.0 -4.5

#类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self

class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()
t.prt()



