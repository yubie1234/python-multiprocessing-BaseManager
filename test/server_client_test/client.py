import sharedmemory 
import random

manager = sharedmemory.get_manager()

dict1 = manager.dict1()

print(dict1)

dict1[random.randint(0,100)] = 1