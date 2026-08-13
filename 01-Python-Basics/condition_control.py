#条件控制
'''
关键字 / 函数	 说明	                                     示例
if	            条件判断语句，当条件为 True 时执行代码块	   if x > 0:
elif	        多条件判断分支（else if）	                 elif x == 0:
else	        所有条件不满足时执行	                     else:
pass	        空语句，占位用，保证语法完整	              if x > 0: pass
match	        结构化模式匹配（Python 3.10+，类似 switch）	  match x: case 1: ...
'''
#if
var1 = 1
if var1:
    print("true")
    print(var1)

var2 = 0
if var2!=1:
    print(var2)

age = int(input("输入你家狗年龄："))
print("")#相当于空一行
if age <= 0:
    print("are you kidding me?")
elif age == 1:
    print("相当 14 岁的人")
elif age == 2:
    print("相当 22 岁的人。")
elif age > 2:
    human = 22 + (age -2)*5
    print("对应人类年龄: ", human)
input("点击 enter 键退出")

#if嵌套
a=1
b=2
if a <= 0:
    print("a<=0")
    if b >= 0:
        print("b >= 0")
    else:
        print("b < 0")
elif a >= 1:
    print("a >= 1")
else:
    print("a大于0且小于1")

#match...case
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401|403|404:#还可以用|设置多个匹配条件
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"

print("\nmatch...case:")
print(http_error(400))
print(http_error(404))
print(http_error(418))
print(http_error(500))


