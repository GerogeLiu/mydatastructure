## mydatastructure
## 常用数据结构及其算法实现

## 线性结构
### 常见线性结构：

### 栈(Stack)

### 队列(Queue)
### 双端队列(Deque)
### 列表(List)


## 编写过程遇到的坑:
1. 判断字符串是否为<u>数字</u>(整数/浮点数)

>>> ***str.isdigit(),内置的isdigit函数只能判断整数，对浮点数是无效的。***

> 最开始想到的就是用float函数来判断，能够使用flaot函数而不报错的话，认为其就是数字，代码如下：

~~~python
def isNumber(s):
	try:
		float(s)
	except ValueError:
		return False
	else:
		return True
~~~
>> 但是，之后发现会出现如下问题，当字符串是'n(N)a(A)n(N)'或'i(I)n(N)f(F)'时，上述代码会得到True的结果。
~~~python
>>> float('nan')
output: nan
>>> float('inf')
output: inf
~~~
>> <font color=red>inf(不区分大小写)</font>表示正无穷，<font color=red>-inf</font>表示负无穷；

>> <font color=green>nan</font>意思为<u> not a Number(不是数)</u>，它不是数，所以无法计算得到具体的值。
更多内容可以点击[链接](https://www.cnblogs.com/malinqing/p/11290131.html)查看。
~~~python
import math

def isNumber(s):
	if math.isnan(s) or math.isinf(s):
		return False
	else:
		try:
			float(s)
		except ValueError:
			return False
		else:
			return True
~~~
>> 为解决两个字符串可能造成误判，上述代码添加判断语句，排除这两个字符串再进行下一步操作。


> 还有一个使用正则表达式匹配的方法：
>>> + [1-9]\d*　     正整数
>>> + -[1-9]\d* 　 负整数
>>> + -?[1-9]\d*　整数
>>> + [1-9]\d*|0　 非负整数
>>> + -[1-9]\d*|0　　 非正整数
>>> + [1-9]\d*\.\d*|0\.\d*[1-9]\d*$　　 正浮点数
>>> + -([1-9]\d*\.\d*|0\.\d*[1-9]\d*)$　 负浮点数
>>> + -?([1-9]\d*\.\d*|0\.\d*[1-9]\d*|0?\.0+|0)$　 浮点数

~~~python
import re

def isNumber(s):
	pattern = re.compile(r'[-+]?[1-9]\d*(\.\d*)?|[-+]?0\.\d*[1-9]\d*|(0\.)?0+$')
	result = pattern.match(s)
	if result:
		return True
	else:
		return False
~~~
>> 有关正则表达式内容查看[链接](https://www.jb51.net/article/166946.htm)以及[这个链接](https://www.jb51.net/article/145009.htm)