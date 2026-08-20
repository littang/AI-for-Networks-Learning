#输出格式美化
'''
Python两种输出值的方式: 表达式语句和 print() 函数。
第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
str()： 函数返回一个用户易读的表达形式。
repr()： 产生一个解释器易读的表达形式。
'''
s = 'hello,li'
print(s)
str(s)
print(repr(s))
print(str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
print(s)

#  repr() 函数可以转义字符串中的特殊字符
hello = 'hello, runoob\n'
hellos = repr(hello)
print(hellos)
# repr() 的参数可以是 Python 的任何对象
print(repr((x, y, ('Google', 'Runoob'))))

#两种方式输出一个平方与立方的表
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用
    print(repr(x*x*x).rjust(4))

for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

#在第一个例子中, 每列间的空格由 print() 添加。
# 这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
# 还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。

#zfill(), 它会在数字的左边填充 0

print('12'.zfill(5))

#str.format() 的使用

print('{}网址： "{}!"'.format('DEEPSEEK', 'www.deepseek.com'))

print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{1} 和 {0}'.format('Google', 'Runoob'))
#引入关键字
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
#位置及关键字参数可以任意的结合
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
#可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
import math
print('常量 PI 的值近似为 {0:.2f}。'.format(math.pi))

#在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Google': 1,'Baidu': 2,'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10}'.format(name, number))

#如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
#也可以通过在 table 变量前使用 ** 来实现相同的功能
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))

#旧式字符串格式化
#% 操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串
print('pi = %5.3f'%math.pi)#但现在使用更加新的str.format


#读键盘输入
#Python 提供了 input() 内置函数从标准输入读入一行文本，默认的标准输入是键盘
'''
str = input("请输入：")
print ("你输入的内容是: ", str)
'''
#读和写文件
#open(filename,mode)
#常见打开模式
'''
r	只读方式打开文件（默认模式），文件必须存在，文件指针位于开头。
w	只写方式打开文件。如果文件存在会被清空；不存在则创建新文件。
a	追加方式打开文件。如果文件存在，写入内容会追加到末尾；不存在则创建新文件。
'''
# f = open("D:/Plan/01-Python-Basics/example.txt","w")

# f.write("How are you?\nI'm fine thank you and you")

# f.close

#文件对象的方法
f = open("D:/Plan/01-Python-Basics/example.txt",'r')

# str = f.read()
# print(str)
# f.close()

# str = f.readline()
# print(str)
# str = f.readline()
# print(str)
# str = f.readline()
# print(str)
# str = f.readline()
# print(str)
# f.close()

# str = f.readlines()
# print(str)
# f.close()

# for line in f:
#     print(line, end = '')
# f.close()


# str = f.readline()
# print(str)
# fu = f.tell()
# print(fu)
# f.close()


'''
seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
seek(x,1) ： 表示从当前位置往后移动x个字符
seek(-x,2)：表示从文件的结尾往前移动x个字符
'''
f = open('D:/Plan/01-Python-Basics/foo.txt', 'rb+')
print(f.write(b'0123456789abcdef'))
print(f.seek(5))
print(f.read(1))
print(f.seek(-3,2))
print(f.read(1))

#当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件。 而且写起来也比 try - finally 语句块要简短
with open('D:/Plan/01-Python-Basics/foo.txt', 'r') as f:
    read_data = f.read()

print(f.closed)

#pickle 模块
#python的pickle模块实现了基本的数据序列和反序列化。



