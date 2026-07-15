#q-5 Write a Program in Python to create a menu-driven fast-food order system using the 'match case' feature.
#For example:
#Press 1 to order a Sandwich
#Press 2 to order a Pizza
#Press 3 to order a Burger
#Extend this program by adding a nested match case for each menu item's
#subtype selection by the user.

#For example:
#Press 1 for Thin Crust Pizza
#Press 2 for Cheese Burst Pizza
#Press 3 for Fresh Dough Pizza

print("----Fast-food Menu----")
print("Press 1 to order a Sandwich")
print("Press 2 to order a Pizza")
print("Press 3 to order a Burger")  

choice = int(input("Enter your choice: "))  

match choice:

    case 1:
        print("\nSandwich Menu")
        print("Press 1 for Veg Sandwich")
        print("Press 2 for cheese Sandwich")
        print("Press 3 for Grilled Sandwich")

        sub = int(input("Enter your choice: "))

        match sub:
            case 1:
                print("You have ordered a Veg Sandwich.")
            case 2:
                print("You have ordered a cheese sandwich.")
            case 3:
                print("You have ordered a Grilled Sandwich.")
            case _:
                print("Invalid choice for Sandwich.")

    case 2:
        print("\nPizza Menu")
        print("Press 1 for Thin Crust Pizza")
        print("Press 2 for Cheese Burst Pizza")

        print("Press 3 for Fresh Dough Pizza")

        sub = int(input("Enter your choice: "))

        match sub:
            case 1:
                print("You have ordered a Thin Crust Pizza.")
            case 2:
                print("You have ordered a Cheese Burst Pizza.")
            case 3:
                print("You have ordered a Fresh Dough Pizza.")
            case _:
                print("Invalid choice for Pizza.")
    case 3:
        print("\nBurger Menu")
        print("Press 1 for Veg Burger")
        print("Press 2 for Cheese Burger")
        print("Press 3 for double patty Burger")

        sub = int(input("Enter your choice: "))

        match sub:
            case 1:
                print("You have ordered a Veg Burger.")
            case 2:
                print("You have ordered a Cheese Burger.")
            case 3:
                print("You have ordered a double patty Burger.")

            case _:
                print("Invalid Burger choice.")


    case _:
        print("Invalid choice for main menu.") 
