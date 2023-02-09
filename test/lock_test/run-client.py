import custommanager as cm
import func
import argparse
parser = argparse.ArgumentParser(description="For Client Run")
parser.add_argument("--with-lock", action='store_true', help="Client Number")
args = parser.parse_args()

def init():
    m = cm.get_manager()
    dict_ = m.dict1()
    lock_ = m.Lock1()
    print(dict_)
    return dict_, lock_

def do_with_lock():
    dict_, lock_ = init()
    func.counting_with_lock(dict_, lock_)
    
def do_without_lock():
    dict_, _ = init()
    func.counting_without_lock(dict_)
    

if __name__ == "__main__":
    if args.with_lock:
        do_with_lock()
    else:
        do_without_lock()
    