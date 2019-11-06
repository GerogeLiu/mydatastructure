#热土豆(约瑟夫)问题
#一共有若干个人，依次数数，数到某个数num的人被淘汰，完成一局；
#接着再从队首开始数，继续这个游戏，直到只剩下一个人为止。

from mypythonds import Queue

#人数--people, 特定的数--num
def hotPotatoes(people, num):
    queue = Queue()
    out_people = []
    for i in range(people):
        queue.enqueue(i+1)
    while queue.size() > 1:
        for j in range(num -1):
            top_people = queue.dequeue()
            queue.enqueue(top_people)
        out_people.append(str(queue.dequeue()))
    print('淘汰顺序:{}'.format('->'.join(out_people)))
    print('最后胜出的是:{}'.format(queue.dequeue()))



if __name__ == '__main__':
    hotPotatoes(30, 7)
        

