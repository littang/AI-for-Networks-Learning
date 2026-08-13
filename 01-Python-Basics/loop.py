'''
关键字 / 函数	 说明	                               示例
for	            迭代循环，用于遍历序列或可迭代对象	     for i in list:
while	        条件循环，条件为 True 时持续执行	    while x > 0:
break	        立即终止当前循环	                   break
continue	    跳过本次循环剩余代码，进入下一次迭代	 continue
else（循环）	循环正常结束（未被 break）时执行	    for i in range(3): ... else: ...
pass	        循环中的占位语句（空操作）	            for i in range(5): pass
range()	        生成整数序列，常与 for 循环配合使用	    range(0, 5)
enumerate()	    遍历时同时获取索引和值	                for i, v in enumerate(list):
'''

#while循环,在 Python 中没有 do..while 循环
'''
while 判断条件(condition)：
    执行语句(statements)……
'''
n=100
conter=0
sum=0
while(conter<=n):
    sum+=conter
    conter+=1
print("1到100的和为：",sum)

#无限循环
#我们可以通过设置条件表达式永远不为 false 来实现无限循环
#你可以使用 CTRL+C 来退出当前的无限循环

#while 循环使用 else 语句
#!/usr/bin/python3
 
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")

#如果你的 while 循环体中只有一条语句，你可以将该语句与 while 写在同一行中

#for语句
'''
for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串
'''
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    print(site)

word = 'runoob'
for letter in word:
    print(letter)

#  1 到 5 的所有数字：
for number in range(1, 6):
    print(number)




#for...else
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#使用break语句
sites = ["Baidu","Google","Taobao","Tenxun"]
for site in sites:
   if site == "Tenxun":
      print("Tenxun")
      break
   print("循环数据" + site)
else:
   print("没有循环数据")
print("完成循环")



#rang()函数
for i in range(0, 10, 3) :
    print(i)

for i in range(-10, -100, -30) :
    print(i)
 
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

aa=list(range(5))
print(aa)

#pass语句
#pass 不做任何事情，一般用做占位语句，如下实例
for letter in 'Runoob': 
   if letter == 'o':
      pass
      print ('执行 pass 块')
   print ('当前字母 :', letter)
 
print ("Good bye!")