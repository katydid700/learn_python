# coding=UTF-8
"""
Python 不会自动调用基类 SchoolMember 的构造函数
你必须自己显式地调用它
形如: SchoolMember.__init__(self, name, age)
相反，如果我们没有在一个子类中定义一个 __init__ 方法
Python 将会自动调用基类的构造函数
"""
class SchoolMember:
    """代表任何学校成员"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("(Initialized SchoolMember:{})".format(self.name))

    def tell(self):
        """告诉我有关我的细节"""
        print('Name:"{}" Age:"{}"'.format(self.name, self.age))

class Teacher(SchoolMember):
    """代表一位老师"""
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print( "(Initialized Teacher: {})".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    """代表一位学生"""
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print( '(Initialized Student:{})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print( 'Marks : "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Louis ', 22, 100)

print()

members = [t, s]
for member in members:
    member.tell()
