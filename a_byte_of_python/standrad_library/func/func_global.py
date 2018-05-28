# coding=UTF-8
"""全局变量
global 语句用以声明 x 是一个全局变量——
因此，当我们在函数中为 x 进行赋值时，
这一改动将影响到我们在主代码块中使用的 x 的值。
"""


x = 50
def func():
    global x
    print('x is ',x)
    x = 2
    print('change global x to ',x)

func()
print('value of x is ', x)