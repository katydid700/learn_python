# coding=UTF-8
"""系统模块
$ python module_using_sys.py we are arguments
The command line arguments are:
module_using_sys.py
we
are
arguments
The PYTHONPATH is ['/tmp/py',
# many entries here, not shown here
'/Library/Python/2.7/site-packages',
'/usr/local/lib/python2.7/site-packages']
在这里要记住的是，运行的脚本名称在 sys.argv 的列表中总会位列第一。因此，在这一案
例中我们将会有如下对应关系： 'module_using_sys.py' 对应 sys.argv[0] ， 'we' 对应
sys.argv[1] ， 'are' 对应 sys.argv[2] ， 'arguments' 对应 sys.argv[3] 。要注意到
Python 从 0 开始计数，而不是 1。
"""
import sys

print('the command line arguments are:')
for i in sys.argv:
        print(i)

print('\n\nthe pythonpath is ', sys.path, '\n')