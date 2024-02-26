#initialization
import math
print('Hello and welcome to the paint job estimator.')
do_calculation = True

while(do_calculation):
    
    do_sqft = True
    do_paint_price = True
    do_another_calculation = True
    
    while (do_sqft):
        try:
            sqft = float(input("Please enter the square feet that is needed to paint: "))
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            print("Good job! You entered a valid value.")
            do_sqft = False
            break
        
    while (do_paint_price):
        try:
            paint_price = float(input("Please enter the price of paint per gallon: "))
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else:
            print("Good job! You entered a valid value.")
            do_sqft = False
            break

    #math
    total_gallons = math.ceil(sqft/350)
    total_labor = total_gallons * 6
    paint_cost = paint_price * total_gallons
    labor_charge = total_labor * 62.25
    
    #output
    print('The number of gallons required is: ', total_gallons)
    print('The number of hours of labor is: ', total_labor, ' hours')
    print('The cost of the paint is: $', paint_cost)
    print('The labor charge is: $', labor_charge)
    print('The total cost is: $', labor_charge + (total_gallons * paint_price))

    #repeat if needed
    while (do_another_calculation):
            try:
                another_calculation = str(input("Would you like to use the paint job estimator again? hit \"y\" for yes: "))
            except ValueError:
                print("The value you entered is invalid. The only valid inputs are characters")
            else:
                do_another_calculation = False
                do_calculation = False
                if (another_calculation == "y"):
                    do_calculation = True
                break

print("Thank you for using the paint job estimator!")
