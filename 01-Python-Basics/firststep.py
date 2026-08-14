print("hello,world")

i = 256*256
print("i的值为",i)

my_list = ["a","b","c","d"]
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])

for i in range(4):
    print(i)

x = 6
if x > 10:
    print("x大于10")
else:
    print("x小于或等于10")


#写一个斐波那契数列
a,b = 0,1
while b < 10:
    print(b)
    a,b = b,a+b#同时赋值太强大了python

#end关键字
#关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符

a,b = 0,1
while b < 1000:
    print(b,end=' ')
    a,b = b,a+b
