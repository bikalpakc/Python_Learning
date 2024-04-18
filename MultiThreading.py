import time
import threading
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    time.sleep(seconds)
    print(f"Sleep done for {seconds} seconds")

# def func2():
#     time.sleep(3)
#     print("Done2")

# def func3():
#     time.sleep(2) 
#     print("Done3")  

# # Executing Normally 
# func(4)
# func(3)
# func(2)

# # Executing using MultiThreading concept
# t1=threading.Thread(target=func, args=4)
# t2=threading.Thread(target=func, args=3)
# t3=threading.Thread(target=func, args=2)

# t1.start()
# t2.start()
# t3.start()


# Executing MultiThreading using ThreadPoolExecutor, so that code becomes less lined, more readable and easy to perform multiple tasks easily at the same time
def Pooling_Demo():
    with ThreadPoolExecutor() as executor:
        thread=executor.submit(func, 4)
        thread=executor.submit(func, 3)
        thread=executor.submit(func, 2)

Pooling_Demo()        