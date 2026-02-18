import sys
def list_operation():
 my_list=[]
 while True:
    print("\nlist Operation")
    print("1.insert an element")
    print("2.delete an element")
    print("3.find an element")
    print("4.Display list")
    print("5.exit")

    choice=int(input("enter your choice "))

    if choice == 1:
        element=input("enter elelment to insert:")
        my_list.append(element)
        print(f"Element'{element}'inserted:")

    elif choice == 2:
        element=input("enter elelment to delete:")
        if element in my_list:
            my_list.remove(element)
            print(f"Element'{element}'deleted:")
        else:
                print(f"Element'{element}'not found:")

    elif choice == 3:
        element=input("enter element to find")
        if element in my_list:
            print(f"lement'{element}'found.")
        else:
            print(f"lement'{element}'not found.")

    elif choice == 4:
        print(f"current list: {my_list}")

    elif choice == 5:
        print("exiting program")
        sys.exit
        break
    
    else:
        print("Invalid choice pls try again")

list_operation()
                
