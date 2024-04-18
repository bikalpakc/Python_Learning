import time
import asyncio

async def function1():
    time.sleep(3)
    print("This is function 1")

async def function2():
    time.sleep(3)
    print("This is function 2")

async def function3():
    time.sleep(3)
    print("This is function 3")

async def main():
    L=await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )            
    print(L)

# //Now all three functions will occur concurrently(parallely), not one by one as they use to by default    