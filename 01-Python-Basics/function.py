#定义一个函数
'''
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号 : 起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。
'''
#say hi
def hi():
    print("hello,world!")

hi()
#比大小
def max(a,b):
    if a > b:
        return a
    else:
        return b

a = 4
b = 6
print(max(a,b))
#计算面积
def area(width,height):
    return width * height
def print_welcome(name):
    print("Welcome",name)

print_welcome("li")
w=4
h=5
print("width = ",w," height = ",h," area = ",area(w,h))

#函数调用

#参数传递
'''
类型属于对象，对象有不同类型的区分，变量是没有类型的
a=[1,2,3]
a="Runoob"
[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，它仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象
'''
'''可更改(mutable)与不可更改(immutable)对象'''

'''
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：
不可变类型：类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
可变类型：类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响
python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
'''
print("python传不可变对象实例")
def change(a):
    print(id(a))
    a = 10
    print(id(a))
a = 1
print(id(a))
change(a)
print("python传可变对象示例")
def changeme( mylist ):
    mylist.append([1,2,3,4])#末尾添加列表元素
    print("函数内取值：",mylist)
    return
mylist = [10,20,30]
changeme( mylist )
print("函数外取值：",mylist)

#参数（必需参数，关键字参数，默认参数，不定长参数）
print("必需参数")
#必需参数
'''
必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样
'''
def printme(str1,a):
    print(str1,a,end = ' ')
    return
printme("string",2)
print()
print("关键字参数")
#关键字参数
'''
关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
'''
def printinfo( name, age ):
    print("name:", name)
    print("age:", age)
    return 
printinfo( age = 50,name = "li")

#默认参数
print("默认参数")
'''
调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值
'''
def printinfo( name, age = 35 ):
   print ("名字: ", name)
   print ("年龄: ", age)
   return

printinfo( age=50, name="runoob" )
print ("------------------------")
printinfo( name="runoob" )

#不定长参数
'''
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名
加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
'''
def printinfo( arg1, *vartuple):
    print("输出：")
    print(arg1)
    print(vartuple)
printinfo( 70, 60, 50 )

def printinfo1( arg1, *vartuple):
    print("输出：")
    print(arg1)
    for var in vartuple:
        print(var)
    return
printinfo1( 10 )
printinfo1( 70, 60, 50 )

#还有一种就是参数带两个星号 **,加了两个星号 ** 的参数会以字典的形式导入
def printinfo2( arg1,**vardict ):
    print("输出：")
    print(arg1)
    print(vardict)
printinfo2(1,d=2,f=3)

#声明函数时，参数中星号可以单独出现,如果单独出现星号 *，则星号 * 后的参数必须用关键字传入
def f(a,b,*,c):
    return a+b+c
print(f(1,2,c=3))


#匿名函数
'''
Python 使用 lambda 来创建匿名函数。
lambda 只是一个表达式，函数体比 def 简单很多。
lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，内联函数的目的是调用小函数时不占用栈内存从而减少函数调用的开销，提高代码的执行速度
'''
#lambda 函数的语法只包含一个语句，如下：
#lambda [arg1 [,arg2,.....argn]]:expression

x = lambda a : a + 10
print(x(5))

sum = lambda arg1,arg2: arg1 + arg2

print("相加后的值：",sum( 10, 20 ))
print("相加后的值：",sum( 10, 30 ))

#我们可以将匿名函数封装在一个函数内，这样可以使用同样的代码来创建多个匿名函数。

def myfunc(n):
  return lambda a : a * n
 
mydoubler = myfunc(2)
mytripler = myfunc(3)
 
print(mydoubler(11))
print(mytripler(11))


#return语句

#强制位置参数，/ 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
#以上例子中形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 和 f 要求为关键字形参

f(10, 20, 30, d=40, e=50, f=60)
#错误示例
#f(10, b=20, c=30, d=40, e=50, f=60)   # b 不能使用关键字参数的形式
#f(10, 20, 30, 40, 50, f=60)           # e 必须使用关键字参数的形式
