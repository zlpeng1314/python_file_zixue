#不接收任何参数的函数
def do_something1():
	print('This is a hello message from do_something().')
do_something1

#没有return语句的函数   示范  p163
def do_something():  #定义个一个名为：do_something的函数
	print('This is a hello message from do_something().')  #打印（这是一封来自do_somethng()的欢迎信息）

if not do_something(): #如果do_something()的返回值为非真，那么：
	print("The return value of 'do_something()' is None")  #打印（这个do_something()的返回值为空）

#接收从外部传递进来的值  p164
def is_leap(year): #定义一个名为is_leap的函数
	leap = False  #默认的leap为False，必须先给变量leap赋值，不然会报警
	if year % 4 == 0: #输入的数值除以4余数为0：
		leap = True   #则输出True
		if year % 100 == 0 and year % 400 != 0: #如果输入的数值除以100余数为零，而且除以400，余数不等于0：
			leap = False                        #则输出False
	return leap  #经过上面的计算后，返回leap的布尔值

print(is_leap(7))
print(is_leap(12))
print(is_leap(100))
print(is_leap(400))

#cpython/Lib/datetime.py是一个更为简洁的版本
def _is_leap(year): #定义一个新的函数 _is_leap()
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) 
	# 返回后面判断结果的布尔值：输入的值除以4等于0，而且（输入的值除以100不等于0，或输入的值除以400等于0）

print(_is_leap(1995))
print(_is_leap(2008))
print(_is_leap(2020))
print(_is_leap(2022))

#一个函数可以接收多个参数，示范  p165
#输出100-9999的之间的斐波那契数列
def fib_between(start, end):   #定义一个函数
	a, b = 0, 1                #这行代码应该就是斐波那契数列的条件设定
	while a < end:             #while循环 a小于设定的第二个值
		if a >= start:         #while循环的陈述，  如果a>=给定的第一个值
			print(a, end=' ')  #打印（a，end从换行转成空格
		a, b = b, a + b        #这行是斐波那契的计算方法：a， b， c（a+b=c）
fib_between(100, 10000)        #设定的斐波那契数列范围在100-9999

print()

#以列表返回设定范围的斐波那契数列  示范1
def fib_between1(start, end):
    r = []                 #设定r为一个空列表
    a, b = 0, 1
    while a < end:
    	if a >= start:
    		r.append(a)    #往列表r里添加对象a
    	a, b = b, a + b    #这一行只能放在这里，移到上面就没有返回结果了
    return r     #这里可以改写成print（r）
print(fib_between1(100, 10000))

print()
#以列表返回设定范围的斐波那契数列   示范2
#不用return ，用print（）输出也行
def fib_between1(start, end):
    r = []
    a, b = 0, 1
    while a < end:
    	if a >= start:
    		r.append(a)
    	a, b = b, a + b
    print(r) 
fib_between1(100, 10000)


#2022年10月30  学习记录

#b变量的作用域   p165
def increase_one(n):   #定义一个函数
    n += 1             #n=n+1 （这个n是局部变量）
    return n           #返回的是n的值

n = 1                  #给全局变量n赋值=1
print(increase_one(n)) #打印自定义的函数内局部变量n的值
print(n)               #打印全局变量n的值

#传递可变容器的错误示范1   p166
def be_careful(a, b):
    a = 2
    b[0] = 'What?!'   #注意  列表里的是0，但实际输出时，列表里1的时候输出了0对应的字符
a = 1
b = [1, 2, 3]
print(be_careful(a, b))   #输出的结果为：None
print(a, b)               #输出的结果为：1 ['What?!', 2, 3]

#传递可变容器的正确 示范1，在函数内部对列表操作之前，创建一个拷贝 p166
def be_careful(a, b):
	a = 2
	b_copy = b.copy()     #对变量b进行拷贝
	b_copy[0] = 'What?!'  #对拷贝的值进行处理

a = 1
b = [1, 2, 3]   
print(be_careful(a, b))  #输出的结果为：None
print(a, b)              #输出的结果为：1 [1, 2, 3]

#2022年10月31日  

#可以接收一系列值的位置参数，*的使用
def say_hi(*names):
	for name in names:
		print(f'Hi, {name}!')
say_hi()  #这一行没有任何输出，因为调用函数的时候没有给它传递任何值
say_hi('ann')
say_hi('mike', 'joho', 'zeo')

def say_hi(*names):  #这里的 * 表示这个names可以接收一系列的值
    for name in names:
        print(f'Hi, {name}!')
names = ('mike', 'joho', 'zeo')
say_hi(*names)   #这里的 * 表示递给函数的是一个容器，打印的字符之间会换行，
say_hi(names)    #不加 * 打印的结果是：Hi, ('mike', 'joho', 'zeo')!  

#调用加 * 的函数时，向它传递任何容器，都会进行同样的处理
def say_hi(*names):  #这里的 * 表示这个names可以接收一系列的值
    for name in names:
        print(f'Hi, {name}!')

a_string = 'python' 
say_hi(*a_string)  #调用字符串
print()
a_range = range(10)
say_hi(*a_range)   #调用范围内的多个数字
print()
a_list = list(range(10, 0, -1))
say_hi(*a_list)    #调用列表
print()
a_dictionary = {'ann':2321, 'mike':8712, 'joe':7610}
say_hi(*a_dictionary) #调用字典

#2022年11月2日 学习记录
#在一个函数里，可以接收一系列值的位置参数只能有一个
#有多个位置参数时，就必须把带 * 的位置参数放在其他位置之后
def say_hi(greeting, *names):   # *names这个位置参数必须放在最后
    for name in names:
        print(f'{greeting}, {name.capitalize()}!') 

say_hi('Hello', 'mike', 'joho', 'zeo')

#为函数的某些参数设定默认值
def say_hi(greeting, *names,capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize() #首字符大写
        print(f'{greeting}, {name}!')

say_hi('Hello', 'mike', 'joho', 'zeo')
print()
say_hi('Hello', 'mike', 'joho', 'zeo',capitalized=True)

#可以接收一系列值的关键字参数
def say_hi(**names_greetings):
    for name, greeting in names_greetings.items(): #以列表返回视图对象
        print(f'{greeting}, {name}!')

say_hi(mike='Hello', ann='Oh,my darling', joho='Hi')

#在调用函数时也可以直接使用字典的形式
def say_hi(**names_greetings):
    for name, greeting in names_greetings.items():
        print(f'{greeting}, {name}!')

a_dictionary = {'mike':'Hello', 'ann':'Oh, my darliing', 'john':'Hi'}
say_hi(**a_dictionary)
print()
say_hi(**{'mike':'Hello', 'ann':'Oh, my darliing', 'john':'Hi'})

#2022年11月4日 学习记录
#定义函数时各种参数的排列顺序  示范1  p171
def say_hi(greeting, *names, capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')

say_hi('Hi', 'mike', 'joho', 'zeo')
say_hi('Welcome', 'mike', 'joho', 'zeo', capitalized=True)

#示范2  给greeting参数设定一个默认值  p172 
def say_hi(greeting='Hello', *names, capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')
#虽然已经给greeting参数设定一个默认值，但是在调用时还是需要给出这个参数
say_hi('Hi', 'mike', 'joho', 'zeo')  
say_hi('Welcome', 'mike', 'joho', 'zeo', capitalized=True)
#say_hi('mike', 'joho', 'zeo') 
#如果不给出greeting参数的设定值，输出结果如下：
#mike, joho!
#mike, zeo!


#正确的写法如下：把加*的位置参数放到设定了默认值的参数的前面
def say_hi( *names, greeting='Hello', capitalized=False):
    for name in names:
        if capitalized:
            name = name.capitalize()
        print(f'{greeting}, {name}!')

say_hi('mike', 'joho', 'zeo')
say_hi('mike', 'joho', 'zeo',greeting='Hi')
#这是因为函数被调用时，面对许多参数，Python 需要按照既定的规则（即，顺序）判定每个参数究竟是哪一类型的参数：
#Order of Arguments（参数的排列顺序）：

#1.Positional （位置）
#2.Arbitrary Positional（任意位置）
#3.Keyword （关键字）
#4.Arbitrary Keyword （任意关键字）

#2022年11月5日 学习记录  #化名与匿名  p175
#化名
def _is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year_leap_bool = _is_leap   #year_leap_bool是 _is_leap 的化名
print(year_leap_bool)       #打印结果：<function _is_leap at 0x0000026603C2E020>
print(year_leap_bool(800))  #打印结果：True

print(id(year_leap_bool))   #id（）是用来查询某对象地址的
print(id(_is_leap))         #他们的返回结果一样：2525430800416

print(type(year_leap_bool)) #type（）是用来查询对象类型的
print(type(_is_leap))       #他们的返回结果一样：<class 'function'>
 
#  用def关键字定义函数和用lambda关键字 定义函数 的示范  p175
#用def关键字定义示范
def add(x, y):
    return x + y
print(add(3, 5))
#用lambda关键字定义示范   lambda就是匿名函数
add = lambda x, y: x + y
print(add(3,5))

#2022年11月6日  学习记录
#python 使用 lambda 来创建匿名函数。
# lambda关键字的:前面的是参数，：之后是表达式，表达式的值就是这个函数的返回值。
# lambda只是一个表达式，函数体比def简单很多。
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
# lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
#虽然 lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

#匿名函数 lambda 官方示范：作为某函数的返回值
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)   #这行之后f的值就等于42了
print(f(0))   #结果是42   这行就是在42的基础上加0
print(f(1))   #结果是43   这行就是在42的基础上加1

# f究竟是什么？
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
print(f)  # 输出结果是：<function make_incrementor.<locals>.<lambda> at 0x000001B3F56D9940>
 # f 不是make_incrementor的化名 ，如果要给这个函取化名，应该这样写：f = make_incrementor ，后面没有（）
print(id(make_incrementor))  #输出结果是：1872428375776
print(id(f))             #输出结果是：1872428374336  他们的系统地址并不一样，说明f不是化名
# lambdda 作为某函数的参数   示范
#写法1
def double_it(n):
    return n * 2
a_list = [1, 2, 3, 4, 5, 6]
b_list = list(map(double_it, a_list))
print(b_list)  #输出结果：[2, 4, 6, 8, 10, 12]

#写法2
c_list = list(map(lambda x: x * 2, a_list))
print(c_list)  #输出结果：[2, 4, 6, 8, 10, 12]
#以上两种写法的结果是一样的，但显然用 lambda关键字比用 def关键字 更为简洁
#map()函数的一个参数是用来接收函数的，第二个参数就是可被迭代的对象
phonebook = [
    {'name':'joho', 'phone':9876},
    {'name':'mike', 'phone':5603},
    {'name':'stan', 'phone':6898},
    {'name':'eric', 'phone':7898},
]
print(phonebook)
print(list(map(lambda  x: x['name'], phonebook)))
print(list(map(lambda  x: x['phone'], phonebook)))


#可以给 map() 传递若干个可被迭代对象：
a_list = [1, 3, 5]
b_list = [2, 4, 6]
print(list(map(lambda x, y: x * y, a_list, b_list))) #输出结果：[2, 12, 30]

#官方教程
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda p: p[1])   #sort（）函数是用来排序的，key是排序的对象
print(pairs)  #输出结果：[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

#2022年11月11日   学习记录  递归函数 ： n 的阶乘演示
def f(n):
    if n == 1:
        return 1   #如果n=1，返回1
    else:
        return n * f(n-1) #否则返回n*f(n-1)
print(f(5))   #打印递归函数f（5）的值，结果是120

#加上一些输出语句，就能更清楚的看到程序的执行流程了
def f(n):
    print('\tn =', n)  #打印n的当前值
    if n == 1:
        print('Returning...')
        print('\tn =', n, 'return:', 1)
        return 1
    else:
        r = n * f(n-1)
        print('\tn =', n, 'return:', r)
        return r
print('Call f(5)...')
print('Get out of f(n), and f(5) =', f(5))
