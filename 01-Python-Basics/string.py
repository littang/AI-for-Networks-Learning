#进度条可视化--------------------------------------------------------------

import time
print("进度条可视化示例：")
for i in range(101): # Loop from 0 to 100
    bar = '[' + '=' * ( i//2 ) + ' ' * ( 100//2 - i // 2) + ']'
    print(f"\r{bar} {i:3}%", end='', flush=True)
    #{i:3}%表示将i格式化为至少3个字符宽度的字符串，并在前面填充空格，以确保输出对齐
    #flush=True表示立即刷新输出缓冲区，以便在每次迭代时立即显示进度条
    time.sleep(0.0005)
print()

#字符串---------------------------------------------------------------
print("\n字符串转义字符示例：")

"""
转义字符    名称	 光标移动方式	                   是否换行
\b          退格	光标向左移动 1 个字符（微调位置）	否
\r	        回车	光标移动到当前行的最开头（行首）	否

\r 跳到开头，从头来写写，适合做整条进度条的刷新。
\b 左挪一步，适合只修改行尾的几个字符。
"""

print("A 的 ASCII 值：", ord('A'))  

print("\x41 为 A 的 ASCII 代码")  
 

decimal_number = 42
binary_number = bin(decimal_number)  
print('42二进制:', binary_number)  

octal_number = oct(decimal_number) 
print('42八进制:', octal_number)  

hexadecimal_number = hex(decimal_number)  
print('42十六进制:', hexadecimal_number)

#字符串运算符
print("\n字符串运算符示例：")
a = "Hello"
b = "Python"
 
print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])
 
if( "H" in a) :
    print("H 在变量 a 中")
else :
    print("H 不在变量 a 中")
 
if( "M" not in a) :
    print("M 不在变量 a 中")
else :
    print("M 在变量 a 中")
 
print (r'\n')
print (R'\n')


#f-string，f 开头，\
# 后面跟着字符串，字符串中的表达式用大括号 {} 包起来，\
# 它会将变量或表达式计算后的值替换进去
print("\nf-string示例：")
name = "Alice"  
age = 30
print(f"My name is {name} and I am {age} years old.")
print("好处就是可以在字符串中直接嵌入变量和表达式\
不用再使用字符串拼接或格式化函数。")
x=1
print(f"{x+1}")   #输出 2
print(f"{x+1=}")  # 输出 x+1=2

#字符串内建函数，略