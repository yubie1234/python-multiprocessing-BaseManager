from .managers import CustomManager

__all__ = ["start_server", "get_manager"]

ip = "127.0.0.1"
port = 50000
address = (ip, port)
authkey = b"abcdefg"


def start_server():    
    manager = CustomManager(address=address, authkey=authkey)
    manager.start()
    return manager

def get_manager(connect=True):
    manager = CustomManager(address=address, authkey=authkey)
    if connect:
        manager.connect()
    return manager
