import custommanager as cm
import time
import argparse

argparse

m = cm.start_server()
# m = cm.get_manager()

m.dict1()["count"] = 0



while True:
    print(m.dict1()["count"], end="\r")
    time.sleep(0.1)