# coding=UTF-8
"""tuple
元组是不可变的
括号内部用逗号隔开
"""
zoo = ('python', 'elephant', 'penguin')
print('number of animals in the zoo is', len(zoo))
new_zoo = 'monkey', 'camel', zoo
print('all naimals in new zoo are', new_zoo)
print('animals brought from old zoo are', new_zoo[2])
print('last animal brought from old zoo is ',new_zoo[2][2])
print('number of animals in the new zoo is ', len(new_zoo)-1+len(new_zoo[2]))