#获取对象信息

#判断类型
>>> type(123)
<class 'int'>
>>> type('str')
<class 'str'>
>>> type(None)
<type(None) 'NoneType'>
#也可以是 自定义的 类

#比较类型
>>> type(123)==type(456)
True
>>> type(123)==int
True
>>> type('abc')==type('123')
True
>>> type('abc')==str
True
>>> type('abc')==type(123)
False

#使用isinstance()  一个对象是否是某种类型，同时还有父子关系，
#能用type()判断的基本类型也可以用isinstance()判断：
>>> isinstance('a', str)
True
>>> isinstance(123, int)
True
>>> isinstance(b'a', bytes)
True

#同时判断两种类型
>>> isinstance([1, 2, 3], (list, tuple))
True
>>> isinstance((1, 2, 3), (list, tuple))
True

#如果要获得一个对象的所有属性和方法，可以使用   dir()   函数，
#它返回一个包含字符串的list，比如，获得一个str对象的  所有属性和方法：

#类似__xxx__的属性和方法在Python中都是有特殊用途的
#比如__len__方法返回长度。
>>> len('ABC')
3
>>> 'ABC'.__len__()
3

>>> class MyDog(object):
...     def __len__(self):
...         return 100
...
>>> dog = MyDog()
>>> len(dog)
100

#以及常用的一些 方法
>>> 'ABC'.lower()
'abc'


#配合getattr()、setattr()以及hasattr()，
#我们可以直接操作一个对象的状态：

>>> class MyObject(object):
...     def __init__(self):
...         self.x = 9
...     def power(self):
...         return self.x * self.x
...
>>> obj = MyObject()

#紧接着，可以测试该对象的属性：
>>> hasattr(obj, 'x') # 有属性'x'吗？
True
>>> obj.x
9
>>> hasattr(obj, 'y') # 有属性'y'吗？
False
>>> setattr(obj, 'y', 19) # 设置一个属性'y'
>>> hasattr(obj, 'y') # 有属性'y'吗？
True
>>> getattr(obj, 'y') # 获取属性'y'
19
>>> obj.y # 获取属性'y'
19
>>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
404


#实例属性与类属性

#给 实例绑定属性 的 方法 是通过 实例变量，或者通过self变量：
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

#Student类本身需要绑定一个属性，这种属性是   类属性
class Student(object):
    name = 'Student'
#这个属性虽然归类所有，但类的所有实例都可以访问到。
>>> class Student(object):
...     name = 'Student'
...
>>> s = Student() # 创建实例s
>>> print(s.name) 
# 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
Student

>>> s.name = 'Michael' # 给实例绑定name属性
>>> print(s.name) 
# 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
Michael
>>> print(Student.name) 
# 但是类属性并未消失，用Student.name仍然可以访问
Student

#在编写程序的时候，千万不要对实例属性和类属性使用相同的名字，
#因为相同名称的  实例属性  将屏蔽掉  类属性

#可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count+=1



#面向对象高级编程

#正常情况下，当我们定义了一个class，创建了一个class的实例后，
#我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：

class Student(object):
    pass

#然后，尝试给实例绑定一个属性：

>>> s = Student()
>>> s.name = 'Michael' # 动态给实例绑定一个属性
>>> print(s.name)
Michael

def set_age(self, age):
   self.=age  age
s.set_age(25)   #这个等效于：s.age=25
#def 后是一个定义的函数，不是属性的名称， 函数内部的赋值对象才是属性


#为了达到限制的目的，Python允许在定义class的时候，
#定义一个特殊的   __slots__   变量，来限制该class实例能添加的属性：
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

>>> s = Student() # 创建新的实例
>>> s.name = 'Michael' # 绑定属性'name'
>>> s.age = 25 # 绑定属性'age'
>>> s.score = 99 # 绑定属性'score'
#由于'score'没有被放到__slots__中，所以不能绑定score属性
#对继承的子类是不起作用的：


#对成绩要求 0-100，进行限制
class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

#Python内置的@property装饰器就是负责把一个方法变成属性调用的：





#多重继承

class Dog(Mammal, Runnable):
    pass
#同时继承两个类即可，
#通过多重继承，一个子类就可以同时获得多个父类的所有功能。
#通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外
#再同时继承Runnable。这种设计通常称之为    MixIn  。


#定制类
#   __str__
>>> class Student(object):
...     def __init__(self, name):
...         self.name = name
...     def __str__(self):
...         return 'Student object (name: %s)' % self.name
... 
>>> print(Student('Michael'))
Student object (name: Michael)

#   __iter__
#如果一个类想被用于for ... in循环，
#类似list或tuple那样，就必须实现一个__iter__()方法 



#调用py文件必须在该目录下使用C:\Users\Admin\PycharmProjects\nsw>python hello.py   的格式











