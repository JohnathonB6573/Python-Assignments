#initialization
print('Hello welcome to the position calculator!')
time = -1
do_calculation = True


while (do_calculation):

    do_initial_position = True
    do_velocity = True
    do_acceleration = True
    do_time = True
    do_another_calculation = True

    #initial position exception handling
    while (do_initial_position):
        try:
            initial_position = float(input("Enter the object's initial position: "))
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            print("Good job! You entered a valid value.")
            do_initial_position = False
            break

    #initial velocitiy exception handling
    while (do_velocity):
        try:
            initial_velocity = float(input("Enter the object's initial velocity: "))
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            print("Good job! You entered a valid value.")
            do_velocity = False     
            break

    #accleration exception handling
    while (do_acceleration):
        try:
            acceleration = float(input("Enter the object's acceleration: "))
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            print("Good job! You entered a valid value.")
            do_acceleration = False
            break

    #time exception handling
    while (do_time):
        try:
            time = float(input("Enter the object's time in seconds:"))
            while time <0:
                print("This value is negative.")
                time = float(input("Enter the object's time in seconds:"))
        except ValueError:
            print("The value you entered is invalid. Only positive numerical values or 0 is valid.")
        else:
            print("Good job! You entered a valid value.")
            math = initial_position + (initial_velocity * time) + (.5 * acceleration * time * time)
            print("final velocity = ", math)
            do_time = False
            break

    #another calculation exception handling
    while (do_another_calculation):
            try:
                another_calculation = str(input("Would you like to use the position calculator again? hit \"y\" for yes: "))
            except ValueError:
                print("The value you entered is invalid. The only valid inputs are characters")
            else:
                do_another_calculation = False
                do_calculation = False
                if (another_calculation == "y"):
                    do_calculation = True
                break

print("Goodbye")
