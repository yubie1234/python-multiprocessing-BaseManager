import custommanager 
import random

manager = custommanager.get_manager()

dict1 = manager.dict1()

print(dict1)

dict1[random.randint(0,100)] = 1