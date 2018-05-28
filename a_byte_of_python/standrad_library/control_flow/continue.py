# coding=UTF-8
"""continue 语句
跳过当前循环块中的剩余语句,并继续该循环的下一次迭代
"""

while True:
    s = input("enter something:")
    if s == "quit":
        break
    if len(s) < 3:
        print( "too small")
        continue
    print(' input is of sufficient length')