import threading
import time
def task1():
    for i in range(3):
        print("task 1:",i)
        time.sleep(1)
def task2():
    for i in range(3):
        print("task 2:",i)
        time.sleep(1)
# create threads
t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)
# start threads
t1.start()
t2.start()
# wait for threads to finish
t1.join()
t2.join()
print("all threads completed")