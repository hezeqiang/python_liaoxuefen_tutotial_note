print('The quick brown fox', 'jumps over', 'the lazy dog');  #输出打印
print('The quick brown fox','\n','jumps over', '\n','the lazy dog');  #输出换行打印


print('100+200=',100+200);  #输出打印，字符串加''号。
A='hello ,world'
print(A[1]);
#会打印出第二个字符，自动变成了字符串
s = 'abcdef'
s[1:5]
#会打印出  第二  到  第六个  元素


'''
多行注释
'''

name=input()  #输入函数，input中输入为字符串   name='world'
print('hello,', name)   #输出打印，name不用引号
name = input('please enter your name: ')   #先显示引号内容再打入字符


'I\'m \"OK\"!'  #I'm "OK"!，\是转义字符,  r''  表示 '' 内部的字符串默认不转义
#\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\

#Python允许用('''...''')的格式表示多行内容,...不用输入，会自动跳出
print('''i
want
fly''')
#will print:
#i
#want
#fly

10/3=3.33333
10%3=1

#强制类型转换：
#  ord()  函数获取字符的整数表示， chr()  函数把编码转换为对应的字符
ord('A')
chr(66)

int(a,16)#16进制字符串转换为十进制,a是字符串
int(a,10)#将十进制字符转化为数字，a是字符串
int(10.9);#浮点数转为整数
float(100)==float('100')#与int不同，可以接收Int和String类型参数的数字，如'100'
int('123')=123
str(1.23)='1.23'
float('12.34')=12.34


# Python的字符串类型是  str 
#为了避免乱码问题，应当始终坚持使用  UTF-8  编码对  str  和  bytes  进行转换。


print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('Hi,','Michael',',you have $' ,1000000)
print('Hi,''Michael'',you have $',1000000)


#如上    %d 整数      %f 浮点数    %s 字符串     %x 十六进制整数  支持强制类型转换
print('%d' % (a))
#注意不可以有  ,  ，而且有一个  %()   的格式
 

#另一种格式化字符串的方法是使用字符串的format()方法，
#它会用传入的参数依次替换字符串内的占位符{0}、{1}等
'Hello, {0}, 成绩提升了 {1}%'.format('小明', 17.125)





classmates = ['Michael', 'Bob', 'Tracy']
#Python内置的一种数据类型是列表：list。
#需要注意到     list    与     数组、字符串   的区别在于有  逗号与单引号    隔开
#list是一种有序的集合，可以随时添加和删除其中的元素。

classmates[0]
#打印出第一个元素：'Michael'
classmates[-2]
#打印出最后第二个元素：'Bob'


#list是一个可变的有序表，
classmates.append('Adam')
#可以往list中追加元素到末尾：
classmates.insert(1, 'Jack')
#在位置1中插入元素，原来的元素后移

classmates.pop(1)
#要删除指定位置的元素，之后的元素前移

classmates[1] = 'Sarah'
#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：

L = ['Apple', 123, True]
#list里面的元素的数据类型也可以不同，字符串、数字、字符（不加引号，不可以打印单个字母）

s = ['python', 'java', ['asp', 'php'], 'scheme']
#list元素也可以是另一个list。



#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，，，其用()来作为符号
classmates = ('Michael', 'Bob', 'Tracy')
#现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。
#因为tuple不可变，所以代码更    安全

#只有1个元素的tuple定义时必须加一个逗号,
t = (1,)

#“可变的”tuple：
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
#对第三个元素的第一个与第二个进行赋值；
#('a', 'b', ['X', 'Y'])

#注意： list 与 tuple 可以相互包含
#str格式的元素不可以改动，但可以打印，  list 与 tuple   元素可以改动，因为加上了  ，
#t[2][0] = 'X'  类似的幅值只可以是元素整个赋值；


#条件判断,如下伸缩，注意有一个  ：  ，结尾的是  else  非  elif
a=20
if a>10:
    print('a is bigger than 10')
elif a<10:
	print('a is smaller than 10')
else:
    print('kid')


#循环
#Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来
#for x in ...循环就是把  每个元素  代入  变量x  ，然后执行缩进块的语句。
sum = 0
for x in range(101):#确定循环次数
    sum = sum + x
print(sum)

#for x in ...循环就是把  每个元素  代入  变量x  ，然后执行缩进块的语句。
L = ['Michael', 'Bob', 'Tracy']
for name in L:
    print(name)


#第二种循环是while循环，只要  条件  满足，就不断循环，条件不满足时退出循环。
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#注意python的  循环  与  判断  是由缩进来判断是否结束的执行语句，都有  ：

#break：作用是提前结束循环。
#可以在循环中用  判断if  来判断是否  跳出循环，break不会跳出 判断if 的
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')



#continue：跳过当前的这次循环，直接开始下一次循环。
#如果我们想只打印奇数，可以用continue语句跳过某些循环：
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)


#’  %  ‘ 是真的好用。





#dict：dict全称dictionary，在其他语言中也称为map，
#使用键-值  （key-value）  存储，具有极快的  查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}  
# key 可以是字符串或数字  ， value 可以是数值或类型是数值的变量 或 字符串 ， 
#只可以用key查找value
print(d['Michael'])mport functools

#修改字典，增加字典条数，（字典的名称是  d ）
d['Adam'] = 67

#删除key与value
d.pop('Bob')

#要避免key不存在的错误，有两种办法，
#一是通过in判断key是否存在：
'Thomas' in d
返回：False

#二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
#判断存在
d.get('Thomas')

#直接幅值语句
d.get('Thomas', -1)

#和list比较，dict有以下几个特点：
#查找和插入的速度极快，不会随着key的增加而变慢；
#需要占用大量的内存，内存浪费多。

#dict的key必须是不可变对象




#set和dict类似，也是一组key的集合，但不存储value。相当于一个list，key不可以重复，
# key 可以是字符串或数字
set([]) 

s = set([1, 2, 3])
#重复元素在set中自动被过滤：
s = set([1, 1, 2, 2, 3, 3])

#通过  add(key)  方法可以添加元素到set中，可以重复添加
s.add(4)

#通过remove(key)方法可以删除元素：
s.remove(4)

#set可以看成数学意义上的  无序  和  无重复元素   的   集合  ，
#因此，两个set可以做数学意义上的  交集、并集  等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)



#再议不可变对象
a = ['c', 'b', 'a']     #显然这是一个list，非 dic、 tuple、  set
a.sort()                #整理元素
a=['a', 'b', 'c']

#对于 str
a = 'abc'
b = a.replace('a', 'A')  #全部替换的
b = 'Abc'
a = 'abc'
#注意 str还是不可以改动的






#函数
#函数查询：http://docs.python.org/3/library/functions.html#abs


#函数定义
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
# def + 函数名 + 引用

#空函数
#现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
    pass

#判断前先检查参数   ：     isinstance()
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

#  return  是指函数的输出结果，可以用  a=my_abs(-5)   的形式引用


#返回多个值
import math
#import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

#引用如下
x, y = move(100, 100, 60, math.pi / 6)
#或者
(x, y) = move(100, 100, 60, math.pi / 6)

#求平方与平方根，注意 ^2 不是正确表达式
pow(b, 2)

#注意在 判断 与 循环中的  ：：：：：：：：：：：符号



#除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，

#位置参数=必选参数


#默认参数
#使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

power(5)=25;      #n=2是默认参数，可以简化函数的调用；降低调用函数的难度。
power(5,3)=125;

#一定要注意  字符串的   ’‘   必须带有，不如是当做变量在引用，会报错

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Adam', 'M', city='Tianjin')   #更改了默认参数



#可变参数
#可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#其中，number可以是   list或者  tuple  ，而且对于元素个数不做要求
calc([1, 2, 3])  #或者
calc((1, 3, 5, 7))

#转变为   可变参数  以后
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#如果利用可变参数，调用函数的方式可以简化成这样：
calc(1, 2, 3)
calc(1, 3, 5, 7)
calc(*nums)  #num是一个  list或者  tuple，之前要加  *
#可以理解为 * 可以把 list或者  tuple 与  直接数据之间相互转换



#关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数，
#这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
#可以如下输入：
person('Adam', 45, gender='M', job='Engineer')
#输出为：  name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
#或者
extra = {'city': 'Beijing', 'job': 'Engineer'}  #这是一个dic
person('Jack', 24, **extra)    #dic前加  **
#输出为：  name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
#它可以扩展函数的功能，比如做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项


#命名关键字参数

#限制关键字参数方法：直接命名：
def person(name, age, *, city, job):  #特定格式，相当于参数名指定的  关键字参数
    print(name, age, city, job)
#命名关键字参数必须传入参数名，没有传入参数名，调用将报错：
#命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
#如果函数定义中已经有了一个可变参数，
#  后面跟着的命名关键字参数就不再需要一个特殊分隔符 * 了：

#必选参数 、  默认参数、  可变参数、  关键字参数  、 命名关键字参数

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
	
>>> f1(1, 2)
a = 1 b = 2 c = 0 args = () kw = {}
>>> f1(1, 2, c=3)
a = 1 b = 2 c = 3 args = () kw = {}
>>> f1(1, 2, 3, 'a', 'b')
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
>>> f1(1, 2, 3, 'a', 'b', x=99)
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
>>> f2(1, 2, d=99, ext=None)
a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}




#递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
#自己调用自己咯，注意要有一个初始值
===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120
#递归函数的优点是定义简单，逻辑清晰。递归调用的次数过多，会导致  栈  溢出。
#理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。

#尾递归：不会出现栈溢出的情况。从第一个初始值开始，每计算一次，计数减一
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
===> fact_iter(5, 1)
===> fact_iter(4, 5)
===> fact_iter(3, 20)
===> fact_iter(2, 60)
===> fact_iter(1, 120)
===> 120



