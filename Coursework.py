import datetime

def display_welcome():
    """
    Display the welcome message for the program.
    """
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("                           Welcome to Land Rental Shop                           ")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def display_menu():
    """
    Displays the main menu.
    """
    print ("1. Show Lands")
    print("2. Rent Land")
    print("3. Return Land")
    print("4. Exit")

def display_exit():
    """
    Display the exit screen.
    """
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("                          Thank you for using Land Rental                          ")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

def return_land_info():
    """
    Read land information from a file and return it as a dictionary.
    """
    land_info = {}
    with open("info.txt", "r") as file:
        for line in file:
            line_elements = line.split(",")
            kitta_number = int(line_elements[0])
            city_district = line_elements[1]
            direction = line_elements[2]
            anna = line_elements[3]
            price = line_elements[4]
            availability = line_elements[5].replace("\n", "")
            land_info[kitta_number] = [city_district, direction, anna, price, availability]
    return land_info

  

def show_lands():
    """
    Print the lands to the screen.
    """
    print("\n")
    print("------------------------------------------------------------------------------------------------------------------")
    print("  Kitta no   Name of City/District    Direction    Anna    Price      Availability")
    print("------------------------------------------------------------------------------------------------------------------")

    land_info = return_land_info()
    for kitta, details in land_info.items():
        print("  ", kitta, "\t  " + "\t".join(details))
    print("-----------------------------------------------------------------------------------------------------------------------\n")


# Validation for kitta number
def valid_kitta(land_info):
    while True:
        try:
            kitta = int(input("Enter kitta number of the land: "))
            if kitta not in land_info:
                print ("INVALID INPUT. Kitta number does not exist.")
                show_lands()
            else:
                return kitta
        except ValueError:
            print("INVALID INPUT. Provide a valid integer for kitta number.")

def valid_quantity(land_info, kitta):
    with open("info.txt", "r") as file:
        for line in file:
            line_parts = line.split(",")
            if line_parts[0] == str(kitta):
                availability = line_parts[5].replace("\n", "")
                found = True
                if availability.lower() == 'available':
                    print(f"Land with Kitta Number {kitta} is available.")
                    print("\n")
                    decision = input("Do you want to purchase it? (yes/no): ").lower()
                    if decision == 'yes':
                        # Proceed with purchase logic
                        print("Purchase completed successfully.")
                        print("\n")
                        return True
                    
                else:
                    print(f"Land with Kitta Number {kitta} is not available for rent. Choose another land.")
                    show_lands()
                    return False
    
    if not found:
        print("Land with kitta number", kitta, "does not exist. Please enter a valid kitta number.")
        show_lands()
        return False


   


def rent_land():
    customer_name = input("Enter your Name: ")
    customer_address = input("Enter your Address: ")
    customer_email = input("Enter your Email: ")
    land_info = return_land_info()
    kitta = valid_kitta(land_info)
    if valid_quantity(land_info, kitta):
        while True:
            try:
                duration = int(input("Enter the duration you want to rent the land (in months): "))
                if duration <= 0:
                    print("Duration must be greater than 0 Months.")
                else:
                    price = int(land_info[kitta][-2])
                    rent = price * duration
                    print("Rent for", duration, "months:", rent)
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer for duration.")


def main():
    display_welcome()
    while True:
        display_menu()
        option = input("Enter your choice: ")
        if option == "1":
            show_lands()
        elif option == "2":
            rent_land()
            
        elif option == "3":
            print("Option 3 is not implemented yet.")
        elif option == "4":
            display_exit()
            break
        else:
            print("INVALID OPTION!! Enter the option from the menu")

main()
