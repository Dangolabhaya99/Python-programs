import sys

def customerManager():
    while (True):
        print("-----------Customer Manager-----------")
        print("1. New Customer")
        print("2. All Customer")
        print("3. Search Customer")
        print("4. Edit Customer")
        print("5. Delete Customer")
        print("0. Exit")
        print("---------------------------------------")
        choice1 =int(input("Enter your choice:"))
        if choice1==1:
            print(" Add New Customer")
        elif choice1 == 2:
            print("All Customer")
        elif choice1==3:
            print("Search Customer")
        elif choice1==4:
            print("Edit Customer")
        elif choice1==5:
            print("Delete Customer")
        elif choice1==0:
            break
        else:
            print("Out of range")

while(True):
    print("-------Main Menu--------")
    print("1. Customer")
    print("2. Driver")
    print("3. Trip")
    print("0. Exit")
    print("------------------------")
    choice = int(input("Enter Your Choice:"))
    print("Your Choice is",choice)
    if choice==1:
        customerManager()
    elif choice==2:
        print("Driver Manager")
    elif choice==3:
        print("Trip Manager")
    elif choice==0:
        print("Bye!!!")
        sys.exit()
    else:
        print("Out of range")

