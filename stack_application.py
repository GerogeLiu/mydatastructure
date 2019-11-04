#栈的运用
# 1、括号的匹配
# 2、中缀表达式转后缀表达式
# 3、后缀表达式的计算
from mypythonds_stack import Stack
import re


#括号匹配
#括号包括三种'([{',如果匹配返回True否则False
def parMatch(T):
    s = Stack()
    balanced = False
    index = 0
    par_dict = {'(':0, ')':0, '[':1, ']':1, '{':2, '}':2}
    while index < len(T) and not balanced:
        if T[index] in '([{':
            s.push(T[index])
        elif T[index] in ')]}' and par_dict[s.peek()] == par_dict[T[index]]:
            s.pop()
        else:
            balanced = True
        index += 1

    if s.isEmpty() and not balanced:
        return True
    else:
        return False


#中缀表达式转成后缀表达式
def toPostfix(exp):
    num = Stack()
    op = Stack()
    result = []




#后缀表达式的计算
def calcPostfix(T):
    s = Stack()
    index = 0
    valid = True
    while index < len(T) and valid:
        if isNumber(T[index]):
            s.push(eval(T[index]))
        elif T[index] in '+-*/':
            if s.size() < 2:
                valid = False
            else:
                num2 = s.pop()  #注意先取出的是第二操作数
                num1 = s.pop()
                if T[index] == '/' and num2 == 0:  #当作除法运算且除数为0时
                    return '除数不能为0'

                else:
                    result = arimetic(num1, num2, T[index])  #调用calculation函数进行计算
                    s.push(result)
        else:
            return '存在无效字符'
        index += 1

    if s.size() == 1 and valid:
        return s.pop()
    else:
        return 'NaN'


#判断字符串为数字(整数或浮点数)
#判断数字的条件稍微严格一些，不接受‘05’这样的字符作为数字
def isNumber(s):
    pattern = re.compile(r'[-+]?[1-9]\d*(\.\d*)?|[-+]?0\.\d*[1-9]\d*|(0\.)?0+$')
    result = pattern.match(s)
    if result:
        return True
    else:
        return False

#四则运算
def arimetic(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '/':
        return round(n1/n2, 3)
    else:
        return n1 * n2

if __name__ == '__main__':
    t = input('输入后缀表达式(空格隔开):')
    print(calcPostfix(t.split()))




    
