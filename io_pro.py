#正则表达式  一种弄定义式  用于判断字符串格式是否匹配

#用\d可以匹配一个数字，\w可以匹配一个字母或数字
#'00\d'可以匹配'007'
#'\d\d\d'可以匹配'010'
#'\w\w\d'可以匹配'py3'；
#.可以匹配任意字符，所以：
#'py.'可以匹配'pyc'、'pyo'、'py!'等等。

#\d{3}表示匹配3个数字，例如'010'；
#\s可以匹配一个空格（也包括Tab等空白符）
#\d{3,8}表示3-8个数字，例如'1234567'

#  \  用于转义
#re模块

s = 'ABC\\-001' # Python的字符串
# 对应的正则表达式字符串变成：
# 'ABC\-001'

s = r'ABC\-001' # Python的字符串
# 对应的正则表达式字符串不变：
# 'ABC\-001'


#正则表达式  在编译时会大量用到

#    网络编程

#客户端
# 导入socket库:
import socket
# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('www.sina.com.cn', 80))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)
# 关闭连接:
s.close()

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)


#服务器
#一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口
#来唯一确定一个Socket。
#简单的服务器程序，它接收客户端连接，把客户端发过来的字符串加上Hello再发回去。
#服务器可能有多块网卡，一个网卡有多个 端口

#127.0.0.1是一个特殊的IP地址，表示本机地址，客户端必须同时在本机运行才能连接
import socket
# 监听端口:
s.bind(('127.0.0.1', 9999))  #9999位自定义的端口
s.listen(5)    #一次传 5 个客户端
print('Waiting for connection...')

#服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接:
while True:
    # 接受一个  新连接:
    sock, addr = s.accept()
    # 创建  新线程  来处理  TCP连接  :
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)







