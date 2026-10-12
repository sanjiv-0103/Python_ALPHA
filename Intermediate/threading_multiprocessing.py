# threading
import threading
def task1():
    print("thread task 1 running")
def task2():
    print("thread task 2 running")
t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)
t1.start()
t2.start()
t1.join()
t2.join()
print("threading completed")

# multiprocessing = separate processes
from multiprocessing import Process
def process1():
    print("process task 1 running")
def process2():
    print("process task 2 running")
if __name__=="__main__":
    p1=Process(target=process1)
    p2=Process(target=process2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("multiprocessing completed")