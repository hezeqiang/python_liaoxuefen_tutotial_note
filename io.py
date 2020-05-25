#错误处理
#高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外

#try     可以使错误程序纠正后完整运行
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:                    #运行try ，如果出错则进入出错的环节，解决之后    继续运行  
        bar('0')
    except ValueError:
        print('ValueError')
    except Exception as e :    #e 可以打印出具体的错误信息
        print('Error:', e)
    finally:
        print('finally...') #在知道错误类型后做什么

#当 try 里面的代码运行出错的时候，将会被 对应错误 的 except 捕获，ValueError、TypeError、ZeroDivisionError只能捕获一种：
#except Exception 能捕获所有错误，


# err.py:
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

main()


# $ python3 err.py
# Traceback (most recent call last):            告诉我们这是错误的跟踪信息。
  # File "err.py", line 11, in <module>         告诉我们调用main()出错了，在代码文件err.py的第11行代码
    # main()
  # File "err.py", line 9, in main              告诉我们调用bar('0')出错了，在代码文件err.py的第9行代码
    # bar('0')
  # File "err.py", line 6, in bar               原因是return foo(s) * 2这个语句出错了
    # return foo(s) * 2
  # File "err.py", line 3, in foo               原因是return 10 / int(s)这个语句出错了，这是错误产生的源头
    # return 10 / int(s)
# ZeroDivisionError: division by zero

#一般源头错误在最下方






#调试  print    assert     logging   以及IDE的自带调试功能

#凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

#assert的意思是，表达式n != 0应该是True，否则，assert语句本身就会抛出AssertionError： n is zero!

#$ python err.py
#Traceback (most recent call last):
#AssertionError: n is zero!




#IO编程              Input/Output       Stream（流）
#Input Stream就是数据从外面 （磁盘、网络） 流进内存，Output Stream就是数据从 内存 流到外面去。
#内存与 cpu 直接相通   同步IO   异步IO   同步和异步的区别就在于是否等待IO执行的结果
 
#使用异步IO来编写程序性能会远远高于同步IO


#——————————————————————————————————————————————————————————————————————
#    硬盘文件操作
f = open('/Users/Admin/1.txt', 'r')
f.read()
'Hello, world!'
f.close()
#可以这样来调用 （并判断文件是否存在， finally在执行），然后关闭
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()

#以下操作自动  open 了对应文件并关闭了 文件
with open('/path/to/file', 'r') as f:
    print(f.read())


#调用readline()可以每次读取一行内容
for line in f.readlines():  # 在遍历所用的行
    print(line.strip())    # 每一行把末尾的'\n'删掉


#读取二进制文件，如图片、视频等等，用'rb'模式打开文件即可：
f = open('/Users/michael/test.jpg', 'rb')
f.read()
b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节

#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
>>> f.read()
#'测试'

#写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
>>> f = open('/Users/michael/test.txt', 'w')
>>> f.write('Hello, world!')
>>> f.close()

#一般会采用以下的语句进行 写入操作
with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!')



#——-——————————————————————————————————————————————————————————————————————————————————
#        内存操作
#StringIO
#很多时候，数据读写不一定是文件，也可以在内存中读写。StringIO顾名思义就是在内存中读写str。
>>> from io import StringIO
>>> f = StringIO()
>>> f.write('hello')   #此时为‘hello’
5
>>> f.write(' ')
1
>>> f.write('world!')   #此时为‘hello world!’  ，也就是说在不断地叠加	
6
>>> print(f.getvalue())
hello world!																	


#逐行 读取一个  内存中的 参数
>>> from io import StringIO
>>> f = StringIO('Hello!\nHi!\nGoodbye!')   #直接赋值初始化
>>> while True:
...     s = f.readline()
...     if s == '':
...         break
...     print(s.strip())
...
Hello!
Hi!
Goodbye!


#BytesIO
#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
#BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
>>> from io import BytesIO
>>> f = BytesIO()
>>> f.write('中文'.encode('utf-8'))
6                      #一般来说一个中文是有六个字符的
>>> print(f.getvalue())
b'\xe4\xb8\xad\xe6\x96\x87'

#请注意，写入的不是str，而是经过UTF-8编码的bytes。
>>> from io import BytesIO
>>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
>>> f.read()
b'\xe4\xb8\xad\xe6\x96\x87'




#操作文件和目录 dir  and cp
#Python内置的os模块也可以直接调用操作系统提供的接口函数

# 重命名文件test1.txt到test2.txt。
os.rename( "test1.txt", "test2.txt" )
#你可以用remove()方法删除文件，需要提供要删除的文件名作为参数。
os.remove(file_name)


#查看当前目录
print (os.getcwd())
'/Users/michael'
# 然后创建一个目录:
os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
os.rmdir('/Users/michael/testdir')
# 换 目录为"C:\\Users\\Admin"
os.chdir("C:\\Users\\Admin")
os.chdir("C:\\Users\\Admin\\PycharmProjects\\crawler")
#要列出当前目录下的所有目录，只需要一行代码：
os.listdir()


#以下是对文件的目录的  字符串  进行操作
#可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
>>> os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')
#os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
>>> os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')
#用于   提取  目录的   相关信息



#进程和线程
#一个任务就是一个进程（Process）
#进程内的这些“子任务”称为线程（Thread）。
#多进程模式；多线程模式；多进程+多线程模式。



#多进程  multiprocessing
























































