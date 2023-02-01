#切片:
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#取前3个元素，应该怎么做？
[L[0], L[1], L[2]]
#升级:
L[0:3]  #等效于  L[:3] 
['Michael', 'Sarah', 'Tracy']
L[-2:]
['Bob', 'Jack']
#取第二个到最后第二个
L[1:-1]
#前10个数，每两个取一个：
L[:10:2]
#所有数，每5个取一个：
L[::5]
#等
r=[]
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
for i in range(3):   #一共循环3次，i 从 0 开始计数，i相比与c语言多了计数功能
    r.append(L[i])

for i in range(100):
    print('hello,world.\nthis is ',i)  #注意range() 中要直接用int类型

#python中for 只可以用 if+break 来中断

#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，
(0, 1, 2, 3, 4, 5)[:3]
#输出：  (0, 1, 2)
#字符串也可以
'ABCDEFG'[:3]
#输出：  'ABC'
#正确1
def trim(s):
    if s[:1] != ' ' and s[-1:] != ' ':  #可以直接判断的，但是必须是 ' ' 形式
        return s
    elif s[:1] == ' ':
        return trim(s[1:])             #嵌套引用
    else :
        return trim(s[:-1])
#正确2
def trim(input):
    if ord(input[0]) == 32:    #由于input[0] 本身带有 '' ，所以不用再加''了
        a=input[1:]
    else:                   #别忘记 else：下的幅值
        a = input
    if ord(input[-1]) == 32:
        b = a[0:-2]
    else:
        b = a
    return b
#以下错误
def trim(input):
    if ord('input[0]') == 32:
        a=input[1:]
    if ord('input[-1]') == 32:
        b = a[0:-1]
    return b



#迭代（Iteration）
#通过for循环来遍历  list或tuple或dict或字符串，这种遍历我们称为迭代（Iteration）
d = {'a': 1, 'b': 2, 'c': 3}   
for key in d:              #d表示dict的key
    print(key)
for value in d.values():    #d.values()表示dict的value
    print(value)
for ch in 'ABC':
    print(ch)
for a in range(32):
    print(a)
#Python内置的enumerate函数可以把一个list变成索引-元素对,也可以直接处理dict，
#注意前一个 i 只表示了排列的次序，不是key
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)
#0 A
#1 B
#2 C


a = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
for i, key in enumerate(a):
	print(i, key)

for i, value in enumerate(a.values()):
	print(i, value)

#for循环可以用 dict 的 items() 函数可以同时迭代    key和value：
for k, v in d.items():
   print(k, '=', v)
x =  A
y =  B
z =  C

for i, value in [(1,'q'),(2,'w'),(3,'e')]:
	print(i, value)
#只要是个对象就可以迭代


>>> for x, y in [(1, 1), (2, 4), (3, 9)]:
...     print(x, y)
...
#1 1
#2 4
#3 9

#isinstance:判断数据类型
>>> a='a'
>>> isinstance(a,str)
True
>>> a=1
>>> isinstance(a,str)
False
>>> a=1
>>> isinstance(a,int)
True
>>> isinstance(a,float)
False
>>> a=1.0
>>> isinstance(a,int)
False
>>> isinstance(a,float)
True




#迭代列表生产器
[x * x for x in range(1, 11)]
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

[x * x for x in range(1, 11) if x % 2 == 0]
#[4, 16, 36, 64, 100]

[m + n for m in 'ABC' for n in 'XYZ']
#['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
#注意字符串的相加就是简单的合并，不会运算

#列出该directory下的文件，相当于 ls
import os # 导入os模块，模块的概念后面讲到
[d for d in os.listdir('.')] # os.listdir可以列出文件和目录


#把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]
#['hello', 'world', 'ibm', 'apple']





#生成器：generator
#这种一边循环一边计算的机制，称为生成器：generator。
g = (x * x for x in range(10))  #L = [x * x for x in range(10)]  改一下[]为 ()

for n in g:
     print(n)
#一般 generator 是使用for循环的

#斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
#用 generator 则是
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
#需要把print(b)改为yield b就可以了：
#每一次迭代调用 fib 中元素时，会从上一次结束的地方开始运行
#yield  等于是  return ，但是可以多次  return  输出值
for x in fib(6):
    print(x)

#又如下
def odd():
    print('step 1')
    yield(1)
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
for x in odd():
    print(x)

#一个函数定义中包含yield关键字，
#那么这个函数就不再是一个普通函数，而是一个generator
#的时变成generator的函数，在每次调用next()候执行，
#遇到 yield 语句返回，再次执行时从上次返回的yield语句处继续执行。
#这意味着  这个函数的结果是   连续的、序列的    
#杨辉三角
def triangles():
    L=[1]
    while True:
        yield L
        L=[L[i]+L[i+1] for i in range(len(L)-1)]
        L.insert(0,1)
        L.append(1)
        if len(L)>20:
            break
    return L
#  len(L)  可以测长度

for i in range(2):
    print(i)
0
1
#注意是从 0 开始的



#迭代器
#我们已经知道，可以直接作用于for循环的数据类型有以下几种：

#一类是集合数据类型，如list、tuple、dict、set、str等；

#一类是generator，包括生成器和带 yield 的generator function。

#这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

#可以使用isinstance()判断一个对象是否是Iterable对象：
isinstance('abc', Iterable)

#而生成器不但可以作用于for循环，还可以被  next()  函数不断调用并返回下一个值，
#直到最后抛出StopIteration错误表示无法继续返回下一个值了。

#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

#可以使用isinstance()判断一个对象是否是Iterator对象：
isinstance((x for x in range(10)), Iterator)

#把list、dict、str等Iterable变成Iterator可以使用iter()函数：
isinstance(iter('abc'), Iterator)

#***********************************************************
for i in range(len(L))       #常用于 for k in range() 循环次数的判断
#**************************************************************





#Python内建了map()和reduce()函数。
#map()函数接收两个参数，一个是函数，一个是Iterable，
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的  Iterator  返回。
#结果可以用  list() 或者 tuple() 变回去

def f(x):
     return x * x
>>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> list(r)
[1, 4, 9, 16, 25, 36, 49, 64, 81]

list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
#这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#适用于迭代计算，同 for   in 
from functools import reduce 
>>> reduce(add, [1, 3, 5, 7, 9])
25



#对于python来说，函数 本身也是一个变量，可以通过  函数名  直接赋给  其他变量



#Python内建的filter()函数用于过滤序列。
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]

#可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。
#注意返回的是一个 iterator ，用list() 返回函数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
#注意这是一个生成器，并且是一个无限序列。
#一般来说 n 是在定义函数的一次循环里面
#然后定义一个筛选函数：
def _not_divisible(n):
    return lambda x: x % n > 0

#最后，定义一个生成器，不断返回下一个素数：
def primes():
	yield 2
	it=_odd_iter()# 初始序列
	while True
		n=next(it)# 返回序列的第一个数
        yield n
		it = filter(_not_divisible(n), it) # 构造新序列



#sorted :用于排列算法

sorted([36, 5, -12, 9, -21])
[-21, -12, 5, 9, 36]
#按照函数输出结果排列，abs是函数名
sorted([36, 5, -12, 9, -21], key=abs)
[5, 9, -12, -21, 36]
#对于字符串按照首字母的ASC码排列
sorted(['bob', 'about', 'Zoo', 'Credit'])
['Credit', 'Zoo', 'about', 'bob']
#要进行反向排序，不必改动key函数，可以传入第三个参数      reverse=True：
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
['Zoo', 'Credit', 'bob', 'about']


#两个 tab 才是 循环判断的正确形式



L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#自定义函数
def by_name(t):
    return str.lower(t[0])
def by_score(t):
    return t[-1]
# key 只表调用的 函数名称
print(sorted(L,key=by_score))   
print(sorted(L,key=by_name))
#注意key引用的函数每一次只处理一个 list 的对象，
#比如第一次key=by_score(('Bob', 75)) ,然后可以通过调用 t[0] 得到具体的排列对象
#就是排列的对象是list ，list的元素是 iterable 的话，可以用iterable[] 取出对象排列
#key 是调用的 function，比如  function()


#返回函数
#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
#调用函数f时，才真正计算求和的结果，否则不会计算
>>> f()
25


#匿名函数
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
map(square, [1,2,3,4,5]) 

map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
# lambda 用于定义匿名函数
>>> f = lambda x: x * x
>>> f
<function <lambda> at 0x101c6ef28>
>>> f(5)
25



#装饰器   decorator
>>> def now():
...     print('2015-3-25')
...
>>> f = now
>>> f()
2015-3-25
#以下方法可以得到 变量函数的函数名
>>> f.__name__
'now'


#装饰器的作用 可以显示出函数的名称、调用时间、运行时长
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-3-25')
#调用
>>> now()
call now():
2015-3-25
#把@log放到now()函数的定义处，相当于执行了语句：
now = log(now)
#log(now) 中调用了now()
#wrapper()函数的参数定义是(*args, **kw)，wrapper()函数可以接受任意参数的调用)
#在wrapper()函数内，首先打印日志，再紧接着调用原始函数。其是一个万能的结果传递器

#decorator本身需要传入参数的话，如下
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

#把 @log 放到now()函数的定义处，相当于执行了语句：
now = log(now)
#这句话把函数输入了日志




#偏函数
#通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。
int('12345', 16)
74565
#16 表示12345是16进制的，int会转化为 10 进制的

#简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），
#返回一个新的函数，调用这个新函数会更简单。
#functools.partial就是帮助我们创建一个偏函数的
>>> import functools
>>> int2 = functools.partial(int, base=2)
>>> int2('1000000')
64
>>> int2('1010101')
85
#偏函数 必须有 函数的默认参数 作为基础










