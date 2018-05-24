# coding=UTF-8
"""if 语句
条件为真,则执行if-block
否则执行else-block
"""
number = 23
guess = int(input('enter an integer:'))

if guess == number:
    # if-block
    print('congratulations, you guessed it')
    print('(but you do not win an prizes!)')
elif guess < number:
    # else-block
    print('no , it is a little higher than that')
else:
    print('no, it is a little lower than that')

print('done')
