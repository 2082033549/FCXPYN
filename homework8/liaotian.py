#4 多进程通讯：
  #编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；  另外一个进程接收并打印消息；
from multiprocessing import Process, Queue

def sender(q):
    print("聊天开始")
    while True:
        m1 = input()
        q.put(m1)
        if m1 == "60":
            break

def receiver(q):
    while True:
        m1 = q.get()
        if m1 == "60":
            print("对话结束")
            break
        print("接收:", m1)


if __name__ == "__main__":
    queue = Queue()  # 消息队列
    p = Process(target=receiver, args=(queue,))
    p.start()
    sender(queue)