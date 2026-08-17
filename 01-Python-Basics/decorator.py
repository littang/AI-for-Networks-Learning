#装饰器（decorator）是 Python 中的一种高级功能，用于在不修改原函数代码的前提下，动态扩展函数或类的功能

#没有参数的装饰器
def my_decorator(func):
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
    return wrapper

@my_decorator
def say_hello():
    print("hello")

say_hello()

#带参数的装饰器
#如果带有参数需要在 wrapper 中使用 *args, **kwargs
def my_decorator1(func):
    def wrapper(*args, **kwargs):
        print("执行前")
        func(*args, **kwargs)
        print("执行后")
    return wrapper

@my_decorator1
def greet(name):
    print(f"Hello,{name}!")

greet("Alice")

#带参数的装饰器（进阶）
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator#注意这里返回的缩进格式，对齐哪一个

@repeat(3)
def say_hi():
    print("hi!")

say_hi()

#类装饰器
'''
类装饰器接收一个类，并返回修改后的类或包装类。
增强类方法
控制实例化过程
实现单例、日志等功能
'''
#函数形式的类装饰器
def log_class(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, name):
            return getattr(self.wrapped, name)

        def display(self):
            print("调用前")
            self.wrapped.display()
            print("调用后")

    return Wrapper

@log_class
class MyClass:
    def display(self):
        print("原方法")

obj = MyClass()
obj.display()

#类形式的类装饰器
class SingletonDecorator:
    def __init__(self,cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
        return self.instance

@SingletonDecorator
class Database:
    def __init__(self):
        print("初始化")

db1 = Database()
db2 = Database()
print(db1 is db2)

#内置装饰器
@staticmethod#定义静态方法
@classmethod#定义类方法
@property#将方法变为属性
class MyClass:
    @staticmethod
    def static_method():
        print("静态方法")

    @classmethod
    def class_method(cls):
        print(cls.__name__)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


#多个装饰器的堆叠
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()













