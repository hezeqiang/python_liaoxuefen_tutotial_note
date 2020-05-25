# Write Python code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

page = '''<div id="top_bin"> <div id="top_content" class="width960">
   <div class="udacity float-left"> <a href="/">'''
#爬虫学习

# Write Python code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

def get_next_target(s):
    start_link = s.find('<a href=')  # 查找括号内字符串的位置，格式是数字
    if start_link == -1:
        return None, 0
    else:
        start_quote = s.find('"', start_link)  # 从 start_link 的位置开始找起
        end_quote = s.find('"', start_quote + 1)  ##从 start_quote 的位置 后一位开始找起
        url = s[start_quote + 1:end_quote]
        return url, end_quote

def print_all_links(page):
    while True:
        url, end_pos = get_next_target(page)
		if url :
			print(url)
			page=page[end_pos:]
		else:
			break

#-------------------——————————————————------------------——————————————————————————————————————————
#注意    True  False   要表示逻辑 必须要第一个字母大写




def get_next_target(s):
    start_link = s.find('<a href=')  # 查找括号内字符串的位置，格式是数字
    if start_link == -1:
        return None, 0
    else:
        start_quote = s.find('"', start_link)  # 从 start_link 的位置开始找起
        end_quote = s.find('"', start_quote + 1)  ##从 start_quote 的位置 后一位开始找起
        url = s[start_quote + 1:end_quote]
        return url, end_quote


def print_all_links(page):
    links=[]
    while True:
        url, end_pos = get_next_target(page)
        if url :
            links.append(url)
            page=page[end_pos:]
        else:
            break
	return links




# def crawl_web(seed,max_depth):
#     tocrawl = [seed]
#     crawled = []
#     next_depth = []
#     depth = 0
#     while tocrawl and depth <= max_depth:
#         page = tocrawl.pop()
#         if page not in crawled:
#             union(next_depth, get_all_links(get_page(page)))
#             crawled.append(page)
#         if not tocrawl:
#             tocrawl, next_depth = next_depth, []
#             depth = depth + 1
#     return crawled

#---------------------------------------------------------------------------------------
#爬取一定深度的url
like
                                   A                        crawled
								/	  \
							B			C					crawled	
						  / |           |
						D   E           F                   tocrawl
				  	   /  \			  / | \
				     H     J        K   L   M               next_depth
#        也就是说  是一次性得到了  一层的所有  url  
#        再开始下一层的检索，   一层一层进行爬虫     
#        在同一层里，   tocrawl 数量只会不断减少




def add_to_index(index,keyword,url):
    a = -1
    for i, value in enumerate(index):           #同时得到了遍历的次数  n-1  以及 value
        if value[0] == keyword:                  #第一个是  关键字  之后是  url 的 list
            a = i
            break
    if a == -1 :
        index.append([keyword])                 #  注意此处  append  的用法，是加入了一个  list  
        a = index.index([keyword])
        index[a].append([url])                  
    else :
        index[a][1].append(url)                    #注意此处  append  的用法
    return index

[['udacity', ['http://udacity.com', 'http://npr.org']], ['computing', ['http://acm.org']]]
#  为了创建这个list   首先遍历查找是否已经有了keyword   没有创建一个   方法如上




s.spilt()   (可以将一个个单词分开)



#------------------------------------------------------------------------------
#  统计出现数
# 2 Gold Stars

# One way search engines rank pages
# is to count the number of times a
# searcher clicks on a returned link.
# This indicates that the person doing
# the query thought this was a useful
# link for the query, so it should be
# higher in the rankings next time.

# (In Unit 6, we will look at a different
# way of ranking pages that does not depend
# on user clicks.)

# Modify the index such that for each url in a
# list for a keyword, there is also a number
# that counts the number of times a user
# clicks on that link for this keyword.

# The result of lookup(index,keyword) should
# now be a list of url entries, where each url
# entry is a list of a url and a number
# indicating the number of times that url
# was clicked for this query keyword.

# You should define a new procedure to simulate
# user clicks for a given link:

# record_user_click(index,word,url)

# that modifies the entry in the index for
# the input word by increasing the count associated
# with the url by 1.

# You also will have to modify add_to_index
# in order to correctly create the new data
# structure, and to prevent the repetition of
# entries as in homework 4-5.


def record_user_click(index,keyword,url):
    urls = lookup(index, keyword)
    if urls:
        for entry in urls:
            if entry[0] == url:
                entry[1] = entry[1]+1


def add_to_index(index, keyword, url):
    # format of index: [[keyword, [[url, count], [url, count],..]],...]
    for entry in index:
        if entry[0] == keyword:
            for urls in entry[1]:
                if urls[0] == url:
                    return
            entry[1].append([url,0])
            return
    # not found, add new keyword to index
    index.append([keyword, [[url,0]]])



def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return '''<html> <body> This is a test page for learning to crawl!
<p> It is a good idea to
<a href="http://www.udacity.com/cs101x/crawling.html">
learn to crawl</a> before you try to
<a href="http://www.udacity.com/cs101x/walking.html">walk</a> or
<a href="http://www.udacity.com/cs101x/flying.html">fly</a>.</p></body></html>'''

        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return '''<html> <body> I have not learned to crawl yet, but I am
quite good at  <a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.
</body> </html>'''

        elif url == "http://www.udacity.com/cs101x/walking.html":
            return '''<html> <body> I cant get enough
<a href="http://www.udacity.com/cs101x/index.html">crawling</a>!</body></html>'''

        elif url == "http://www.udacity.com/cs101x/flying.html":
            return '<html><body>The magic words are Squeamish Ossifrage!</body></html>'
    except:
        return ""
    return ""

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None


#Here is an example showing a sequence of interactions:
index = crawl_web('http://www.udacity.com/cs101x/index.html')
print lookup(index, 'good')
#>>> [['http://www.udacity.com/cs101x/index.html', 0],
#>>> ['http://www.udacity.com/cs101x/crawling.html', 0]]
record_user_click(index, 'good', 'http://www.udacity.com/cs101x/crawling.html')
print lookup(index, 'good')
#>>> [['http://www.udacity.com/cs101x/index.html', 0],
#>>> ['http://www.udacity.com/cs101x/crawling.html', 1]]




import time
time.clock
#记录系统时间以及可以用于计算 算法 花费的时间
def time_execution(code):
    start=time.clock()
    result=eval(code)
    end=time.clock()
    return result ,start-end



chr(ord('a')) = a
字符与asc转化
a=97
A=65


population={'Shanghai':17.8,'Istanbul': 13.3,'Karachi':13.0,'Mumbai':12.5}
print(population['Shanghai'])
17.8

#dic 会自动排序
element={}
element['h']={'a':97,'b':98}      #在一个空的dic中  添加   新的 key-value， 不用append的，直接加
                                  #并且这个 value 也是一个 dic
        key      value

可以调用以下
element['h']['b']  
>>>98

def involved(courses, person):
    list={}
    for semster in courses:
        for course in courses[semster]:
            for people in courses[semster][course]:
                if courses[semster][course][people]==person:
                    if semster in list:
                        list[semster].append(course)
                    else:
                        list[semster]=[course]
    print(list)

