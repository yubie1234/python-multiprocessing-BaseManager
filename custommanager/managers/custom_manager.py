import multiprocessing
import threading
from multiprocessing.managers import BaseManager, DictProxy, AcquirerProxy
import os

class CustomManager(BaseManager):
    pass

# Dict Test
def shared_dict(shared_dict={}):
    return shared_dict

CustomManager.register("dict1", shared_dict, DictProxy) # 공유 O
CustomManager.register("dict2", dict, DictProxy) # 공유 X
sd = {}
CustomManager.register("dict3", lambda: sd, DictProxy) # 공유 O


# Lock Test
tl = threading.Lock()
CustomManager.register("Lock1", lambda: tl, AcquirerProxy)

print(os.getpid())
