def counting_without_lock(dict_):
    for i in range(10000):
        current_ = dict_["count"]
        dict_["count"] += 1
        next_ = dict_["count"]
        if next_ - current_ != 1:
            pass
#             print("Wrong", next_ - current_)
            
def counting_with_lock(dict_, lock_):
    for i in range(10000):
        with lock_:
            current_ = dict_["count"]
            dict_["count"] += 1
            next_ = dict_["count"]
            if next_ - current_ != 1:
                pass
#                 print("Wrong", next_ - current_)