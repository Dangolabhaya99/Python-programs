import sys

while(True):
    print("-----------Main Menu-----------")
    print("1. Insert Driver")
    print("2. Display All Drivers")
    print("3. Search Driver")
    print("4. Edit Driver")
    print("5. Delete Driver")
    print("0. Exit")
    print("-------------------------------")
    Choice = int(input("Enter your choice:"))
    print("-------------------------------")
    print("Your choice :", Choice)
    if Choice==0:
        print("Bye!")
        sys.exit() #program exit
    elif Choice>=6 or Choice<0:
        print("Choice out of range")
    elif Choice==1:
        print("Insert driver")
    elif Choice==2:
        print("Display All Drivers")
    elif Choice==3:
        print("Search Driver")
    elif Choice==4:
        print("Edit Driver")
    elif Choice==5:
        print("Delete Driver")