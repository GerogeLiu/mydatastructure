#栈的实现:采用python的基础类型列表，进行实现
#栈，先进后出

class Stack():
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        return len(self.stack) == 0
    def push(self, c):
        self.stack.append(c)
    def pop(self):
        return self.stack.pop()   #没有return,返回值为None
    def size(self):
        return len(self.stack)
    def peek(self):
        return self.stack[-1]

#队列的实现
#队列，先进先出
class Queue():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()


if __name__ == '__main__':
    '''
    #测试上述数据结构的功能是否与想要的一致
    s = Stack()  #初始化一个栈对象
    print(s.isEmpty()) #判断对象是否为空
    s.push(3)  #向栈对象s中添加一个整数3
    s.push(7)
    s.push(2)
    print(s.size())  #size方法返回栈对象的长度
    print(s.pop())        #pop方法移除栈顶元素
    print(s.size())
    print(s.peek())  #peek方法‘窥视’栈顶元素

    s.push(11)
    print(s.peek())
    print(s.isEmpty())
'''

    q = Queue()
    print(q.isEmpty())
    q.enqueue(4)
    q.enqueue('a')
    q.enqueue(True)
    print(q.isEmpty())
    print(q.size())
    print(q.dequeue())
    print(q.size())


