from driver import Driver
from ManageDriver import saveDriver,searchDriver,deleteDriver,updateDriver,allDrivers

# Test-1
# d1 = Driver() # declare and initialize object
# d1.setDID(1) # set values
# d1.setName("Aryan Rai")
# d1.setLicenseNo("BS1000091")
# saveDriver(d1) # save drive info

# Test-2
# did = name = lno = None
# did = int(input("Enter ID : "))
# name = input("NAME : ")
# lno = input("LICENSE NO : ")
# d2 = Driver(did, name, lno)
# saveDriver(d2)

# Check whether driver record found or not
# driver = searchDriver(69695)
# if len(driver) == 0:
#     print("Record not found")
# else:
#     print(driver)

# Update
# driver2=Driver(1,'Dangol','123456')
# result = updateDriver(driver2)
# print(result)

# Delete
# result=deleteDriver(2)
# print(result)

# All Driver
result=allDrivers()
print(result)