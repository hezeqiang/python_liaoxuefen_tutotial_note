# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.
print (s[0:3]+t[4:9])
#or print (s[0:3]+t[-4:])





# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the first occurrence of 'hoo'
# in the value of text, or -1 if
# it does not occur at all.
text = "first hoo"

hoo_test=text.find('hoo')
if hoo_test>0:
    print(hoo_test)
else:
    print(-1)





# You may assume x is not negative.
# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'
# Along with the str function, this problem can be solved 
# using just the information introduced in unit 1.
# x = 3.14159 
# >>> 3 (not 3.0)
# x = 27.63 
# >>> 28 (not 28.0)
# x = 3.5 
# >>> 4 (not 4.0)
x = 3.14159
#ENTER CODE BELOW HERE
y=str(x+0.5)  #简易的四舍五入
x=y[:y.find('.')]
print(x)





# Example 1
marker = "AFK"
replacement = "away from keyboard"
line = "I will now go to sleep and be AFK until lunch time tomorrow."

marker_position=line.find(marker)
length=len(marker)
replaced =line[0:marker_position]+replacement+line[marker_position+length:]
print replaced

#注意line[0:2]  是指从0到2-1的位置的字符 
#以及  len(string) 的应用




#找到第二个位置
def find_second(a , b):
    first_position=a.find(b)
    second_position=a.find(b,first_position+1)
    return second_position
twister = "she sells seashells by the seashore"
print(find_second(twister,'she'))




#可以有两个  return
def is_friend(a):
        if a[0] == 'D' or  a[0] == 'N' :
            return True
        else:
            return False
# 判断中  用  or    和    and




def print_numbers(a):
    i=0
    while i<=a:
        print (i)
        i=i+1
        if i==2:
            break
#   break  在loops中使用  if


def pro(a,b)：
	if a==1：
		return a
	return b
#注意这里最后只会返回一个 值， 
#也就是说，   def中遇到了return  之后马上返回，不再运行下去了




def stamps(n):
    a=n//5
    b=(n%5)//2
    c=(n-a*5-2*b)
    return a, b, c

print (stamps(8))
(1, 1, 1)
#在python中     %是取余    //是取整除     /是精确除法



def fix_machine(debris, product):
    x = 1
    m= "Give me something that's not useless next time."
    for a in product:
        q =debris.find(a)
        x=x*(q+1)
    if x==0:
        return m
    return product
#  for 的应用在字符串的查找





#查询 b元素是否在 a数组中， 如果无，返回-1
def find_element(a,b):
     if b not in a  :        # 判断是否a存在b
         return -1
     else :
         return a.index(b)       #a.index(b)     返回 第一个b元素 在a数组中的序号 





#  append  的使用
a= [1,2,3]
b = [2,4,6]
a.append(b)
print(a)
#               [1, 2, 3, [2, 4, 6]]


def union(a, b) :
    for i in b:   #遍历b
        if i not in a:
            a.append(i)
    return a
#                [1, 2, 3, 4, 6]




#  pop  堆栈  不断推出最后一个元素 
a = [1,2,3]
for i in range(3):    
    x=a.pop()
    print(x)



#创建一个空的  数组  
a = []




#查找 list 最大值
def greatest(list_of_numbers):
    if list_of_numbers:                       #如果这个  数组 不是一个   空数组
        a=0
        for i in list_of_numbers:
            if i>a:
                a=i
        return a
    else :
        return 0





def numbers_in_lists(string):
    result=[]

    small=[]
    for i in range(len(string)):
        if i== 0:
            result.append(int (string[0]))
            biggest = int (string[0])
        else :
            str = int(string[i])
            if  str > biggest:
                if small != []:
                    result.append(small)
                result.append(str)
                biggest= str
                small=[]
            else:
                small.append(str)
    if small != []:
        result.append(small)
    return  result

string = '543987'
result = [5,[4,3],9,[8,7]]
print repr(string), numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result

#主要的思想是   通过不断的替换最大值来判断继续 append 的是哪个数组






#-----------------------------------------------------------------------
#           对于自建空数组的合法操作是  append
#               不可以直接赋值
a=[]
#a[0]=1
a.append(1)





#   chr(i)      进行asc码转换
list=[chr(i) for i in range(97,123)]
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

