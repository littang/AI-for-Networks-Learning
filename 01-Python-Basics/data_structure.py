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




