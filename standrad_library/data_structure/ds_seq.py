# coding=UTF-8
"""sequence序列
列表、元组、字符串可以看作序列
序列的主要功能是资格测试(membership test)
和索引操作(indexing operations)
在切片操作中，第一个数字（冒号前面的那位）指的是切片开始的位置，
第二个数字（冒号后面的那位）指的是切片结束的位置。
你要记住如果你希望创建一份诸如序列等复杂对象的副本（而非整数这种简单的对象
（Object）），你必须使用切片操作来制作副本。如果你仅仅是将一个变量名赋予给另一个名
称，那么它们都将“查阅”同一个对象，如果你对此不够小心，那么它将造成麻烦。
"""

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'

print('item 0 is', shoplist[0])
print('item 1 is', shoplist[1])
print('item 2 is', shoplist[2])
print('item 3 is', shoplist[3])
print('item -1 is', shoplist[-1])
print('item -2 is', shoplist[-2])

print('item 1 to 3 is', shoplist[1:3])
print('item 2 to end is', shoplist[2:])
print('item 1 to -1 is ', shoplist[1:-1])
print('item start to end is ', shoplist[:])

print('characters 1 to 3 is ', name[1:3])
print('characters 2 to end is ', name[2:])
print('characters 1 to -1 is ', name[1:-1])
print('characters start to end is ', name[:])