'''
列表是最常用的 Python 数据类型，它可以作为一个方括号内的逗号分隔值出现。
列表的数据项不需要具有相同的类型
创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。
'''
#更新列表
list = ['Google', 'Runoob', 1997, 2000]
print("更新前列表 : ", list)
list[2] = 2001
print("更新后列表 : ", list)
#append() 方法用于在列表末尾添加新的对象。该方法无返回值
list.append('baidu')
print("添加元素后列表 : ", list)


#删除列表元素
del list[1],list[3]
# 先删除索引为 1 的元素
# 然后再删除当前列表（注意是变化后!的列表）中索引为 3 的元素
print("删除元素后列表 : ", list)

#列表脚本操作符
'''
Python 表达式	                         结果	                         描述
len([1, 2, 3])	                        3	                            长度
[1, 2, 3] + [4, 5, 6]	                [1, 2, 3, 4, 5, 6]              组合
['Hi!'] * 4	                            ['Hi!', 'Hi!', 'Hi!', 'Hi!']	重复
3 in [1, 2, 3]	                        True	                        元素是否存在于列表中
for x in [1, 2, 3]: print(x, end=" ")	1 2 3	                        迭代
依次从列表 [1, 2, 3] 中逐个取出元素，每次取一个赋值给 x，然后把这个 x 打印出来，后面跟一个空格。
'''

#列表截取与拼接
#与字符串操作类似
L=['Google', 'Runoob', 'Taobao','baidu']
L
print(L)        #输出完整列表
print(L[2])      # 输出列表的第三个元素
print(L[-2])     # 输出列表的倒数第二个元素
print(L[1:])     # 输出从第二个元素开始后的所有元素
print(L[1:3])    # 输出从第二个元素开始到第三个元素

#嵌套列表
nested_list = [['Google', 'Runoob'], ['Taobao', 'baidu']]
print(nested_list)  # 输出嵌套列表
print(nested_list[0])  # 输出第一个子列表
print(nested_list[0][1])  # 输出第一个子列表的第二个元素

#列表比较
import operator
a = [1, 2, 3]
b = [1, 2, 4]
c = [1, 2, 3]
print("operator.eq(a,b): ",operator.eq(a, b))  # False
print("operator.eq(a,c): ",operator.eq(a, c))  # True

#列表函数
'''
1	len(list)
列表元素个数
2	max(list)
返回列表元素最大值
3	min(list)
返回列表元素最小值
4	list(seq)
将元组转换为列表
'''

#列表方法
'''
1	list.append(obj)
在列表末尾添加新的对象
2	list.count(obj)
统计某个元素在列表中出现的次数
3	list.extend(seq)
在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4	list.index(obj)
从列表中找出某个值第一个匹配项的索引位置
5	list.insert(index, obj)
将对象插入列表
6	list.pop([index=-1])
移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7	list.remove(obj)
移除列表中某个值的第一个匹配项
8	list.reverse()
反向列表中元素
9	list.sort( key=None, reverse=False)
对原列表进行排序
10	list.clear()
清空列表
11	list.copy()
复制列表
'''

#方法和函数的区别
'''
函数：
独立调用，直接写名字，把数据当作“原料”塞进括号里。
格式：函数名(要处理的数据)
属于 Python 全局命名空间
通常不修改原数据，而是创建一个新的副本并返回

方法：
依附于对象，通过点号（.）调用，数据在前面“主动”调用自己的技能。
格式：数据.方法名()
属于 特定的类（Class）只有该类对象才能用
通常直接修改原数据（原地操作），且返回 None
'''


'''
Python 的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号 ( )，列表使用方括号 [ ]。
元组创建只需要在括号中添加元素，并使用逗号隔开即可
'''
#元组的创建
tup1 = ()#空元组
tup2 = (50,)#一个元素的元组，不加逗号会被当作数学计算中的括号使用

#访问元组：类似列表的访问方式

#元组中的元素不允许修改或删除，但可以对元组进行连接组合或删除整个元组
 
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
 
# 以下修改元组元素操作是非法的。
# tup1[0] = 100
 
# 创建一个新的元组
tup3 = tup1 + tup2
print (tup3)

# tup = ('Google', 'Runoob', 1997, 2000)
 
# print (tup)
# del tup
# print ("删除后的元组 tup : ")
# print (tup)
#以上实例元组被删除后，输出变量会有异常信息输出

# 元组运算符
# 与字符串一样，元组之间可以使用 +、+=和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。


#元组索引和截取，略

#元组内置函数'
'''
1	len(tuple)
元组元素个数
2	max(tuple)
返回元组元素最大值
3	min(tuple)
返回元组元素最小值
4   tuple(iterable)
将可迭代对象转换为元组
'''


#元组不可变性
#不支持修改，重新赋值的元组 tup，绑定到新的对象了，不是修改了原来的对象，内存地址也变了


'''
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值 key=>value 对用冒号分割，
每个对之间用逗号分割，整个字典包括在花括号 {} 中 

键必须是唯一的，但值则不必。创建时如果同一个键被赋值两次，后一个值会被记住
值可以取任何数据类型，但键必须是不可变的，如字符串，数字。列表就不行
'''
#dict 作为 Python 的关键字和内置函数，变量名不建议命名为 dict

#创建字典

# 使用大括号 {} 来创建空字典
emptyDict = {}
#使用内建函数 dict() 创建字典
emptyDict1 = dict()

print(emptyDict)
# 查看字典的数量
print("Length:", len(emptyDict))
# 查看类型
print(type(emptyDict))

#访问字典里的值
tinydict={'name':'li','Age':19}
print("tinydict['name']:",tinydict['name'])
print("tinydict['Age']:",tinydict['Age'])

#修改键值对
tinydict['Age'] = 20
tinydict['School'] = 'BUPT'
print(tinydict)

#删除字典元素
#del tinydict['Name'] # 删除键 'Name'
tinydict.clear()     # 清空字典
del tinydict         # 删除字典

#字典内置函数和方法
'''
len(dict)
str(dict)以字符串输出字典，包括花括号
type(variable)返回dict类型
'''
'''
1	dict.clear()
删除字典内所有元素
2	dict.copy()
返回一个字典的浅复制
3	dict.fromkeys()
创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
4	dict.get(key, default=None)
返回指定键的值，如果键不在字典中返回 default 设置的默认值
5	key in dict
如果键在字典dict里返回true，否则返回false
6	dict.items()
以列表返回一个视图对象
7	dict.keys()
返回一个视图对象
8	dict.setdefault(key, default=None)
和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
9	dict.update(dict2)
把字典dict2的键/值对更新到dict里
10	dict.values()
返回一个视图对象
11	dict.pop(key[,default])
删除字典 key（键）所对应的值，返回被删除的值。
12	dict.popitem()
返回并删除字典中的最后一对键和值。
'''


'''
集合（set）是一个无序的不重复元素序列。
集合中的元素不会重复，并且可以进行交集、并集、差集等常见的集合操作。
可以使用大括号 { } 创建集合，元素之间用逗号 , 分隔， 或者也可以使用 set() 函数创建集合。
'''
#列表的创建
set()#空列表必须用set(),而非{}
parame = {"value01",'value02'}
set1 = {1,2,3,4}
set2 = set([4,5,6,7])

#添加元素
set1.add("sa")
print(set1)#无顺序

set1.update({114,514},[77,99])#另一种添加元素的方法
print(set1)
#移除元素
set2.remove(5)
print(set2)

set2.discard(7)#另一种一处的方法
print(set2)

#随机删除
thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
x = thisset.pop()

print("删掉了: ",x)
print("还剩下:",thisset)

#计算集合元素个数
aa=len(set1)
print(aa)

#清空集合
#set.clear()

#集合内置方法
'''
add()	为集合添加元素
clear()	移除集合中的所有元素
copy()	拷贝一个集合
difference()	返回多个集合的差集
difference_update()	移除集合中的元素，该元素在指定的集合也存在。
discard()	删除集合中指定的元素
intersection()	返回集合的交集
intersection_update()	返回集合的交集。
isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	判断指定集合是否为该方法参数集合的子集。
issuperset()	判断该方法的参数集合是否为指定集合的子集
pop()	随机移除元素
remove()	移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	返回两个集合的并集
update()	给集合添加元素
len()	计算集合元素个数
'''



