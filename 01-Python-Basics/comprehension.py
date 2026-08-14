#python推导式
print("list")
#列表推导式
'''
[表达式 for 变量 in 列表] 
[out_exp_res for out_exp in input_list]
or
[表达式 for 变量 in 列表 if 条件]
[out_exp_res for out_exp in input_list if condition]
'''
names = ['Bob','Tom','Jacky','Jason','Smith','Jerry','Wendy']
new_name = [name.upper() for name in names if len(name)>3]
print(new_name)

print("dict")
#字典推导式
'''
{ key_expr: value_expr for value in collection }
or
{ key_expr: value_expr for value in collection if condition }
'''
listdemo = ['Google','Baidu','Beiyou']
#将列表中的字符为键，字符串的长度为值，组成键值对
newdict = {key:len(key) for key in listdemo}
print(newdict)

print("set")
#集合推导式
'''
{ expression for item in Sequence }
or
{ expression for item in Sequence if conditional }
'''
setnew = {i**2 for i in(1,2,3)}
print(setnew)

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
print(type(a))

print("tuple")
#元组推导式（生成器表达式）
#元组推导式和列表推导式的用法也完全相同，只是元组推导式是用 () 圆括号将各部分括起来、
# 而列表推导式用的是中括号 []，另外元组推导式返回的结果是一个生成器对象。
'''
(expression for item in Sequence )
or
(expression for item in Sequence if conditional )
'''
a = (x for x in range(1,11))
print("返回生成器对象：",a,"\n类型",type(a))
print(tuple(a)) # 使用 tuple() 函数，可以直接将生成器对象转换成元组


