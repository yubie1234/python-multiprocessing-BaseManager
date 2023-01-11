import custommanager 

manager = custommanager.get_manager(connect=False)
server = manager.get_server()
server.serve_forever()

