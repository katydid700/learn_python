# coding=UTF-8
"""break 语句
用于中断语句的执行
"""

while True:
    s = input("enter something:")
    if s == 'quit':
        break
    print( 'length of the string is ' )
    print(len(s))
print('done')

