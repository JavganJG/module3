opcion = int(0)
list = []
while True:
    print("MENU")
    print("------------------------------")
    print("1.-Add a number to the list")
    print("2.-Add a number in a position in the list")
    print("3.-Show the length of the list")
    print("4.-Delete the last number in the list")
    print("5.-Delete a number in the list")
    print("6.-Count numbers")
    print("7.-Positions of a numbers")
    print("8.-Show the list")
    print("9.-Exit")
    print("------------------------------")
    opcion = int(input("Choose an option: "))
    if(opcion==1):
        list.append(int(input("Choose a number: ")))
    elif(opcion==2):
        position = int(input("Choose a position: "))
        number = int(input("Choose a number: "))
        if position <= len(list):
            list.insert(position,number)
        else:
            print("Incorrect position")
    elif(opcion==3):
        print(len(list))
    elif(opcion==4):
        if len(list) > 0:
            del list[-1]
        else:
            print("Any element in the list")
    elif(opcion==5):
        if len(list) > 0:
            position = int(input("Select a position to delete: "))
            if position <= len(list):
                list.pop(position)
            else:
                print("Incorrect position")   
        else:
            print("Any element in the list")
    elif(opcion==6):
         print(list.count(int(input("Select the number: "))))
    elif(opcion==7):
        num = int(input("Choose a number: "))
        for elem in list: 
            es = False
            if num == elem:
                es = True
        if es == True:
            print(list.index(num))
    elif(opcion==8):
        print(list)
    elif(opcion==9):
        break
    else:
        print("Choose a correct option")
       