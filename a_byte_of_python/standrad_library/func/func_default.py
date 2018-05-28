# coding=UTF-8
"""默认参数值
默认参数值应该是常数。
更确切地说，默认参数值应该是不可变的
"""

def say(message,times=1):
    print (message * times)

say('hello')
say('world',5)