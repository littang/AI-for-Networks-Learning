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
#self 不是 python 关键字，我们把他换成其他的也是可以正常执行的
class Test:
    def prt(iii):
        print(iii)
        print(iii.__class__)
 
t = Test()
t.prt()

class MyClass:
    def __init__(self,value):
        self.value = value

    def display_value(self):
        print(self.value)

obj = MyClass(42)
obj.display_value()
#在上面的例子中，self 是一个指向类实例的引用，
# 它在 __init__ 构造函数中用于初始化实例的属性，
# 也在 display_value 方法中用于访问实例的属性。
# 通过使用 self，你可以在类的方法中访问和操作实例的属性，从而实现类的行为。


#类的方法，就是用def关键自定义的，且第一个参数必为self的函数
class people:
    name = ''
    age = 0
    #以上为基本属性
    __weight = 0
    #两个下划线开头为私有属性，类的外部无法访问

    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s say: I'm %d years old"%(self.name,self.age))


#实例化类
# p = people('li',10,20)
# p.speak()
        
#单继承示例
class student(people):
    grade = ''
    def __init__(self, n, a, w, g):
        people.__init__(self,n, a, w)
        self.grade = g
    def speak(self):
        print('%s 说：我%d岁了，%d年纪在读'%(self.name,self.age,self.grade))

s = student('ken',10,60,3)
s.speak()


#另一个类，多继承之前的准备
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

#多继承
class sample(speaker,student):
    a = ''
    def __init__(self, n, a, w, g, t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test = sample("Tim",25,80,4,"python")
test.speak()

class Father:
    def myMethod(self):
        print("调用父类方法")

class Child(Father):
    def myMethod(self):
        print("调用子类方法")

c = Child()
c.myMethod()
super(Child,c).myMethod()

#类的私有属性实例
class JustCounter:
    __secretCount = 0
    publicCounter = 0

    def count(self):
        self.__secretCount += 1
        self.publicCounter += 1
        print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCounter)
#print(counter.__secretCount)#报错，AttributeError: 'JustCounter' object has no attribute '__secretCount'

#类的私有方法实例
class Site:
    def __init__(self,name,url):
        self.name = name
        self.__url =url

    def who(self):
        print("name :",self.name)
        print("url :",self.__url)

    def __foo(self):
        print("this is private way")

    def foo(self):
        print("this is public way")
        self.__foo()
        
x = Site("菜鸟教程",'www.xxx.com')
x.who()
x.foo()
#x.__foo()
'''
类的专有方法：
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__truediv__: 除运算
__mod__: 求余运算
__pow__: 乘方
'''

#运算符重载
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector(%d %d)'%(self.a,self.b)

    def __add__(self,other):
        return Vector(self.a + other.a,self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print(v1 + v2)


















