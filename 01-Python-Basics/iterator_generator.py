#迭代器
'''
代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，
直到所有的元素被访问完结束。
迭代器只能往前不会后退。
字符串，列表，元组对象都可以用于创建迭代器
'''

list = [1,2,3,4]
it = iter(list)
print(next(it))
for x in it:
    print(x,end = ' ')

print(" ")

#使用next函数
import sys

list1 = [1,2,3,4]
it1 = iter(list)

# while True:
#     try:
#         print(next(it1))
#     except StopIteration:
#         sys.exit()#此函数用于强制退出代码


#创建一个迭代器
#创建一个返回数字的迭代器，初始值是1，逐步增加1
class MyNumber:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myClass = MyNumber()
myiter = iter(myClass)

for x in myiter:
    print(x)

#生成器
'''
使用了 yield 的函数被称为生成器（generator）
yield 是一个关键字，用于定义生成器函数，生成器函数是一种特殊的函数，可以在迭代过程中逐步产生值，而不是一次性返回所有结果。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
当在生成器函数中使用 yield 语句时，函数的执行将会暂停，并将 yield 后面的表达式作为当前迭代的值返回。
然后，每次调用生成器的 next() 方法或使用 for 循环进行迭代时，函数会从上次暂停的地方继续执行，直到再次遇到 yield 语句。这样，生成器函数可以逐步产生值，而不需要一次性计算并返回所有结果。
调用一个生成器函数，返回的是一个迭代器对象。
'''


def countdown(n):
    while n > 0 :
        yield n
        n -= 1

generator = countdown(5)

print(next(generator))
print(next(generator))

for value in generator:
    print(value)


#用生成函数实现斐波那契数列
import sys

def fibonacci(n):
    a,b,counter = 1,1,0
    while True:
        if(counter > n):
            return
        yield a
        a,b = b,a+b
        counter += 1
f = fibonacci(10)

while True:
    try:
        print(next(f),end = ' ')
    except StopIteration:
        sys.exit()




