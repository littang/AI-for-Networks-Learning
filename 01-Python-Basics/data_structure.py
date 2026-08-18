#列表
#列表是可变的，而字符串和元组不行
'''
方法	            描述
list.append(x)	    把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
list.extend(L)	    通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list.insert(i, x)	在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
list.remove(x)	    删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
list.pop([i])	    从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。）
list.clear()	    移除列表中的所有项，等于del a[:]。
list.index(x)	    返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
list.count(x)	    返回 x 在列表中出现的次数。
list.sort()	        对列表中的元素进行排序。
list.reverse()	    倒排列表中的元素。
list.copy()	        返回列表的浅复制，等于a[:]。
'''
#类似 insert, remove 或 sort 等修改列表的方法没有返回值。

#将列表当作栈使用，以下是栈操作
# 压入（Push）: 将一个元素添加到栈的顶端。
# 弹出（Pop）: 移除并返回栈顶元素。
# 查看栈顶元素（Peek/Top）: 返回栈顶元素而不移除它。
# 检查是否为空（IsEmpty）: 检查栈是否为空。
# 获取栈的大小（Size）: 获取栈中元素的数量。

#1创建一个空栈
stack = []
#2压入（Push）操作
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
#3弹出（Pop）操作
top_element = stack.pop()
print(top_element)
print(stack)
#4查看栈顶元素（Peek/Top）
top_element = stack[-1]
print(top_element)
#5检查是否为空（IsEmpty）
is_empty = len(stack) == 0
print(is_empty)
#6获取栈的大小（Size）
size = len(stack)
print(size)

#将列表当作队列使用
'''
在 Python 中，列表（list）可以用作队列（queue），但由于列表的特点，直接使用列表来实现队列并不是最优的选择。
队列是一种先进先出（FIFO, First-In-First-Out）的数据结构，意味着最早添加的元素最先被移除。
使用列表时，如果频繁地在列表的开头插入或删除元素，性能会受到影响，因为这些操作的时间复杂度是 O(n)。为了解决这个问题，Python 提供了 collections.deque，它是双端队列，可以在两端高效地添加和删除元素。
'''
#使用 collections.deque 实现队列
from collections import deque

queue = deque()

queue.append('a')#a先进入
queue.append('b')
queue.append('c')

print("队列状态：",queue)
#移除队首元素
first_element = queue.popleft()#a先被移除，如果用pop(),那就是c被移除，那就不是队列了，是栈了
print("移除的元素:", first_element)
print("队列状态:", queue)  
#查看队首元素
front_element = queue[0]
print("队首元素：",front_element)
#检查是否为空
is_empty = len(queue) == 0
print("is queue empty:",is_empty)
#获取队列大小
size = len(queue)
print("queue's size:",size)

#使用列表实现队列
#差不多，但需要注意，列表底层是靠动态数组实现的，而collections.deque底层是一个双向链表
#collections.deque 不要求元素在内存中连续存储。因此，在两端（左端或右端）进行添加或弹出操作时，只需要修改少数几个指针的指向，不受队列大小的影响，时间复杂度恒为O(1)
#使用list在需要频繁地通过索引随机访问元素、需要进行大量的切片（slicing） 操作、实现一个栈（LIFO），只从尾部（append和pop）操作数据等情况下更方便

#1创建队列
queue = []
#2向队尾添加元素
queue.append('a')
queue.append('b')
queue.append('c')
print("队列状态:", queue)  
#3从队首移除元素
#使用 pop(0) 方法从队首移除元素：
first_element = queue.pop(0)
print("移除的元素:", first_element)  
print("队列状态:", queue)            
#4查看队首元素（不移除）
front_element = queue[0]
print("队首元素:", front_element)   
#5检查队列是否为空
is_empty = len(queue) == 0
print("队列是否为空:", is_empty)     
size = len(queue)
print("队列大小:", size)            

#列表推导式
vec = [2,4,6]
print("vec = ",vec)
vec1 = [x*3 for x in vec]
print("vec1 = ",vec1)
vec2 = [[x,x**2] for x in vec]
print("vec2 = ",vec2)

vec3 = [3*x for x in vec if x > 3]
print("vec3 = ",vec3)


freshfruit = [' banana','  loganberry ','passion fruit  ']
freshfruit1 = [weapon.strip() for weapon in freshfruit]
print(freshfruit1)
print(freshfruit)#推导式是生成了一个新的，原来的改不了，字符串不可变性

vv = [2,4,6]
vc = [4,3,-9]
print(vv)
print(vc)
vp1 = [x*y for x in vv for y in vc]
print(vp1)
vp2 = [vv[i]*vc[i] for i in range(len(vv))]
print(vp2)

#嵌套列表解析
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
matrix_ = [[row[i] for row in matrix] for i in range(4)]
print(matrix)
print(matrix_)
#也可以用以下方法实现
matrix__ = []
for i in range(4):
    matrix__row = []
    for row in matrix:
        matrix__row.append(row[i])
    matrix__.append(matrix__row)

print(matrix__)

#del语句
'''
使用 del 语句可以从一个列表中根据索引来删除一个元素，
而不是值来删除元素。这与使用 pop() 返回一个值不同。
可以用 del 语句从列表中删除一个切割，或清空整个列表
（我们以前介绍的方法是给该切割赋一个空列表）
'''
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[:]
print(a)

#元组和序列
t = 1234,4321,'bonjuor'
print(t[0])
print(t)
u = t,(1,2,3,4,5)
print(u)
'''
元组在输出时总是有括号的，以便于正确表达嵌套结构。
在输入时可能有或没有括号， 不过括号通常是必须的
（如果元组是更大的表达式的一部分）
'''

#集合
'''
集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；
后者创建一个空的字典，下一节我们会介绍这个数据结构。
'''

basket = {'apple','orange','apple','pear','orange','banana'}
print("{'apple','orange','apple','pear','orange','banana'}")
print(basket)
print('apple'in basket)

a = set('abandon')
b = set('banana')
print(a)
print(a - b)#在a不在b
print(b - a)
print(a|b)#在a或b
print(a&b)#在a和b都有
print(a^b)#在a或b中，但不同时在

#集合也支持推导式

aa = {x for x in 'abandonnn' if x not in 'ajsandfn'}
print(aa)

#字典
'''
序列是以连续的整数为索引，
与此不同的是，字典以关键字为索引，
关键字可以是任意不可变类型，
通常用字符串或数值
一对大括号创建一个空的字典：{}
'''
tel = {'jack': 4098, 'sape': 4139}
tel['gay'] = 4432
print(tel)
print(tel['jack'])
del tel['sape']
tel['lily'] = 4127
print(tel)
print(list(tel.keys()))
print(sorted(tel.keys()))
print('jack' in tel)
print('sape' in tel)

#构造函数dict()直接从键值对元组列表中构建字典
dictiona = dict([('space',4444),('safe',3333),('haha',2222)])
print(dictiona)

#此外，字典推导可以用来创建任意键和值的表达式词典
aaa = {x:x**2 for x in (2,4,6)}
print(aaa)
#如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便
aaaa = dict(sape=4139, guido=4127, jack=4098)
print(aaaa)



#遍历技巧
print("遍历技巧")

#在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
     print(k, v)

#在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
for i,v in enumerate(['tic','tac','toe']):
    print(i,v)

#同时遍历两个或更多的序列，可以使用 zip() 组合
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数
for i in reversed(range(1,10,2)):
    print(i)

#要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)




