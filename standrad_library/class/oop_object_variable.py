# coding=UTF-8
"""对象变量（Object variable）
由类的每一个独立的对象或实例所拥有
每个对象都拥有属于它自己的字段的副本
也就是说，它们不会被共享
也不会以任何方式与其它不同实例中的相同名称的字段产生关联
"""


class Robot:
    "这个是类变量"
    population = 0

    def __init__(self, name):
        self.name = name
        print("(Initializing {})".format(self.name))
        Robot.population += 1

    def die(self):

        print("{} is being destroyed ".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one . ".format(self.name))
        else:
            print("There are still {:d} robots working".format(Robot.population))

    def say_hi(self):

        print("Greetings, my masters call me {}".format(self.name))

    @classmethod
    """
    how_many 实际上是一个属于类而非属于对象的方法
    你可以将装饰器想象为调用一个包装器（Wrapper）函数的快捷方式
    因此启用 @classmethod 装饰器等价于调用：
    how_many = classmethod(how_many)
    """
    def how_many(cls):
        """当前人口数量"""
        print("we have {:d} robots.".format(cls.population))



droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3P0")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here. \n")

print("Robots have finished their work . so let's destroy them")

droid1.die()
droid2.die()

Robot.how_many()