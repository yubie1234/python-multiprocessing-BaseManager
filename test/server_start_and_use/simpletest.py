import sharedmemory 

server = sharedmemory.start_server()

manager1 = sharedmemory.get_manager()
manager2 = sharedmemory.get_manager()
manager3 = sharedmemory.get_manager()
manager4 = sharedmemory.get_manager()

m1_dict1 = manager1.dict1()
m2_dict1 = manager2.dict1()
m3_dict1 = manager3.dict1()
m4_dict1 = manager4.dict1()

m1_dict1["AAA"] = 1
m1_dict1["BBB"] = 1
m1_dict1["CCC"] = 1

print(m1_dict1, m2_dict1, m3_dict1, m4_dict1)


for i in range(10):
    m1_dict1["AAA"] += 1
    print(m1_dict1, m2_dict1, m3_dict1, m4_dict1)