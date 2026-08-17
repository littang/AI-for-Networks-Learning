#lambda匿名函数 可以有任意数量的参数，但只能有一个表达式
'''
lambda 函数是匿名的，它们没有函数名称，只能通过赋值给变量或作为参数传递给其他函数来使用。
lambda 函数通常只包含一行代码，这使得它们适用于编写简单的函数。

语法格式：
lambda arguments: expression
lambda是 Python 的关键字，用于定义 lambda 函数。
arguments 是参数列表，可以包含零个或多个参数，但必须在冒号(:)前指定。
expression 是一个表达式，用于计算并返回函数的结果。
'''

x = lambda a,b : a * b
print(x(5,6))
y = lambda a,b,c : a * b * c
print(y(2,3,4))

#lambda 函数通常与内置函数如 map()、filter() 和 reduce() 一起使用，以便在集合上执行操作
numbers = [1,2,3,4,5,6]
squared = list(map(lambda x: x**2,numbers))
print(squared)
even_numbers = list(filter(lambda x: x % 2 == 0,numbers))
print(even_numbers)
from functools import reduce
product = reduce(lambda x,y: x * y,numbers)
print(product)














