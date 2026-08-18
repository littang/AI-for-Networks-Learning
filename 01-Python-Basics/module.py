#模块
'''
Python 中的模块（Module）是一个包含 Python 定义和语句的文件，文件名就是模块名加上 .py 后缀。
模块可以包含函数、类、变量以及可执行的代码。通过模块，我们可以将代码组织成可重用的单元，便于管理和维护。
'''
'''
代码复用：将常用的功能封装到模块中，可以在多个程序中重复使用。
命名空间管理：模块可以避免命名冲突，不同模块中的同名函数或变量不会互相干扰。
代码组织：将代码按功能划分到不同的模块中，使程序结构更清晰。
'''
import sys
 
print('命令行参数如下:')
for i in sys.argv:
   print(i)
 
print('\n\nPython 路径为：', sys.path, '\n')

#import 语句
#一个模块只会被导入一次，不管你执行了多少次 import。这样可以防止导入模块被一遍又一遍地执行。

#from … import 语句
#Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：

#给模块起别名
import numpy as np  # 将 numpy 模块别名设置为 np
from math import sqrt as square_root  # 将 sqrt 函数别名设置为 square_root


#from … import * 语句
#把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：

from modname import *
#不推荐，容易引起命名冲突。

#深入模块

#__name__ 属性
'''
一个模块被另一个程序第一次引入时，其主程序将运行。
如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用 __name__ 属性来使该程序块仅在该模块自身运行时执行。
'''
#eg：
# Filename: using_name.py
# if __name__ == '__main__':
#    print('程序自身在运行')
# else:
#    print('我来自另一模块')
# $ python using_name.py
# 程序自身在运行

# $ python
# >>> import using_name
# 我来自另一模块
# >>>
'''
说明：每个模块都有一个 __name__ 属性。
如果模块是被直接运行，__name__ 的值为 __main__。
如果模块是被导入的，__name__ 的值为模块名。
说明：__name__ 与 __main__ 底下是双下划线
'''
#dir函数
#内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回

#标准模块
'''
模块名	功能描述
math	数学运算（如平方根、三角函数等）
os	操作系统相关功能（如文件、目录操作）
sys	系统相关的参数和函数
random	生成随机数
datetime	处理日期和时间
json	处理 JSON 数据
re	正则表达式操作
collections	提供额外的数据结构（如 defaultdict、deque）
itertools	提供迭代器工具
functools	高阶函数工具（如 reduce、lru_cache）
'''
#包
'''
包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 
目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。
最简单的情况，放一个空的 :file:__init__.py就可以了。当然这个文件中也可以包含一些初始化代码或者为（将在后面介绍的） __all__变量赋值。


'''
# 用户可以每次只导入一个包里面的特定模块，比如:

# import sound.effects.echo
# 这将会导入子模块:sound.effects.echo。 他必须使用全名去访问:

# sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
# 还有一种导入子模块的方法是:

# from sound.effects import echo
# 这同样会导入子模块: echo，并且他不需要那些冗长的前缀，所以他可以这样使用:

# echo.echofilter(input, output, delay=0.7, atten=4)
# 还有一种变化就是直接导入一个函数或者变量:

# from sound.effects.echo import echofilter
# 同样的，这种方法会导入子模块: echo，并且可以直接使用他的 echofilter() 函数:

# echofilter(input, output, delay=0.7, atten=4)
# 注意当使用 from package import item 这种形式的时候，对应的 item 既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量。

# import 语法会首先把 item 当作一个包定义的名称，如果没找到，再试图按照一个模块去导入。如果还没找到，抛出一个 :exc:ImportError 异常。

# 反之，如果使用形如 import item.subitem.subsubitem 这种导入形式，除了最后一项，都必须是包，而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字。




#从一个包中导入*
#略
