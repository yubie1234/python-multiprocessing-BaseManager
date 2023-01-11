from .managers import CustomManager

__all__ = ["start_server", "get_manager"]

ip = "127.0.0.1"
port = 50000
# address = (ip, port)
authkey = b"abcdefg"


def start_server(ip=ip, port=port, authkey=authkey):
    address = (ip, port)
    manager = CustomManager(address=address, authkey=authkey)
    manager.start()
    return manager

def get_manager(ip=ip, port=port, authkey=authkey, connect=True):
    address = (ip, port)
    manager = CustomManager(address=address, authkey=authkey)
    if connect:
        manager.connect()
    return manager
