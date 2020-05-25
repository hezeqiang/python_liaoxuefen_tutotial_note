#模块
#此处查看http://docs.python.org/3/library/functions.html
mycompany
 ├─ web
 │  ├─ __init__.py
 │  ├─ utils.py
 │  └─ www.py
 ├─ __init__.py
 ├─ abc.py
 └─ xyz.py
 
 
#为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）。
#文件www.py的模块名就是mycompany.web.www
#mycompany 是package


#使用模块，典型模块
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，
#第2行注释表示.py文件本身使用标准UTF-8编码；

' a test module '
#第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
__author__ = 'Michael Liao'
#第6行使用__author__变量把作者写进去
import sys
#导入sys模块
def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

#关于sys.argv函数，移步https://www.cnblogs.com/aland-1415/p/6613449.html
#Sys.argv[ ]其实就是一个列表，里边的项为用户输入的参数，
#关键就是要明白这参数是从程序外部输入的，而非代码本身的什么地方
#运行1.py shuishuide 获得的sys.argv就是['hello.py', 'shuishuide']。

#当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，
#而如果在其他地方导入该hello模块时，if判断将失败，用于模块直接运行测试

#一个模块可能不止一个函数，调用hello.test()时，才能打印出Hello, word!

#类似__xxx__这样的变量是特殊变量，可以被直接引用，
#但是有特殊用途，比如上面的__author__，__name__就是特殊变量

#类似_xxx和__xxx这样的函数或变量就是非公开的（private），
#不应该被直接引用，比如_abc，__abc等；
#一般用于函数的函数，  多次封装
def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)



#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    print(sys.argv)
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

#面向对象最重要的概念就是类（Class）和实例（Instance）
#在Python中，定义类是通过class关键字
class Student(object):
    pass

#class后面紧接着是类名，即Student
#定义好了Student类，就可以根据Student类创建出Student的实例
#创建实例是通过 类名+() 实现的：
>>> bart = Student()
>>> bart
<__main__.Student object at 0x10a67a590>
>>> Student
<class '__main__.Student'>
#变量bart指向的就是一个Student的实例，
#后面的0x10a67a590是内存地址，每个object的地址都不一样
#可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：
>>> bart.name = 'Bart Simpson'
>>> bart.name
'Bart Simpson'

#通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
#注意到__init__方法的第一个参数永远是self，表示创建的实例本身
#把各种属性绑定到self，因为self就指向创建的实例本身。
#有了__init__方法，在创建实例的时候，就不能传入空的参数了，
#必须传入与__init__方法匹配的参数
>>> bart = Student('Bart Simpson', 59)
>>> bart.name
'Bart Simpson'
#和普通的函数相比，在类中定义的函数只有一点不同，
#就是第一个参数永远是实例变量self

#数据封装。
#这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))
#可以直接调用 实例 的函数，函数在类里面定义了
>>> bart.print_score()
Bart Simpson: 59

#封装的另一个好处是可以给Student类增加新的方法，比如get_grade：

class Student(object):
    ...

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
#分类并封装

#命令行运行py：
#cmd中运行，不要进入python中，进入指定文件夹
#>cd\Users\Admin\PycharmProjects\nsw
#输入python hello.py   或者  python hello.py shuishuide 即可


#限制访问

#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
#实例的变量名如果以__开头，就变成了一个私有变量（private），

class Student(object):

    def __init__(self, name, score):  #属性绑定专用函数
        self.__name = name            #属性在实例后面加上 .
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))
#也就是所谓的 不能复制，
#注意，参数永远是 self，也就是实例 实例在 _init_中的第一个参数

>>> bart = Student('Bart Simpson', 59)
>>> bart.__name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Student' object has no attribute '__name'

#只有内部可以访问，外部不能访问
#但是如果外部代码要获取name和score怎么办？
#可以给Student类增加   get_name  和   get_score
class Student(object):
    ...

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

#虽然我可以被访问，但是，请把我视为私有变量，不要随意访问


#在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），
#而被继承的class称为基类、父类或超类（Base class、Super class）。

class Animal(object):
    def run(self):
        print('Animal is running...')
#当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：
class Dog(Animal):
    pass

class Cat(Animal):
    pass

#当子类和父类都存在相同的run()方法时，
#子类的run()会覆盖了父类的run()，继承的另一个好处：多态。

a = list() # a是list类型
b = Animal() # b是Animal类型
c = Dog() # c是Dog类型

#类似于list的定义
>>> isinstance(b, Animal)
True
>>> isinstance(c, Dog)
True

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
sorted(L, key=lambda x: x[0])	
#其主要过程是：匿名函数返回每一个L的元素（是tuple）的第一个元素
#这还是匿名函数的一个重要的用处，一般    需要输入一个函数
#比如 sorted、reduce、map等	



class Student(object):

    def __init__(self, namezhi, scorezhi):
        self.name = namezhi
        self.score = scorezhi

    def set_score(self, score):
        if 0 <= score <= 100:
            self.score = score
        else:
            raise ValueError('bad score')

    def set_name(self, name):
        self.name = name

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

#如上 一个类有许多个 属性，比如 
art = Student('Simpson', 59)
#则有 art.name  art.score art.set_score art.set_name 
#每个属性可以进行赋值，赋值的对象就是属性的 值
art.score=99
#art.__score  是私有的属性，不可被访问
#set_name 与 name 是两个不同的属性
#_int_() 里面对应的是两个一开始就必须赋值的  值， 属性是
# self.name 与self.score

#def 的函数也是实例的  方法 ，其与属性类似，可以直接引用，但不可赋值

























