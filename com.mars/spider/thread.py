import _thread
from com.mars.db import *

# 为线程定义一个函数
def print_time( threadId ):
    print(threadId)
    insert("insert into t_score (`name`, subject, fraction) values ( '%s' ,'%s', %d)" % ('name', 'subject', threadId))

# 创建两个线程
if __name__ == "__main__":
    try:
        for i in range(1,5000):
           _thread.start_new_thread(print_time, (i, ))
    except:
       print ("Error: 无法启动线程")

    while 1:
       pass