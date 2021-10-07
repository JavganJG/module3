code ="TRWAGMYFPDXBNJZSQVHLCKE"
while True:
    dni = input("Validate DNI: ")
    letter = dni[-1].upper()
    numbers = dni[:-1]
    if(len(dni)-1 ==8 and numbers.isdigit()):
        int(numbers)
        mod = numbers%23
        if letter == code[mod]:
            print("The DNI is correct")
            True
        else:
            print("The DNI not's correct")
            False
    else:
        
        print("The DNI not's complete")
        False
