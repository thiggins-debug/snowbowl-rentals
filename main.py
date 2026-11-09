# Teddy Higgins
# SnowBowl Montana Rental Shop - Week 2
# These are sample prices and quantities, not actual SnowBowl data.
# Data is only stored while the program is running this week.

equipment = {
    "adult_ski_set": {"price": 40.00, "total": 15, "available": 13},
    "junior_ski_set": {"price": 30.00, "total": 10, "available": 8},
    "performance_ski_set": {"price": 55.00, "total": 8, "available": 6}
}


# Prints all the menu options from the app plan.
def show_menu():
    print("\n--- SnowBowl Montana Rental Shop ---")
    print("1. View equipment")
    print("2. Add equipment")
    print("3. Record a rental")
    print("4. Close the day")
    print("5. View rental report")
    print("6. Run simulation")
    print("7. Save and exit")


# Prints each equipment type and all of its details.
def view_equipment():
    print("\n--- Equipment ---")
    for name in equipment:
        item = equipment[name]
        print("\nEquipment:", name)
        print(f"Daily price: ${item['price']:.2f}")
        print("Total quantity:", item["total"])
        print("Available quantity:", item["available"])


# Keeps asking until the user enters a positive whole number.
def get_quantity():
    while True:
        try:
            quantity = int(input("Number of sets to add: "))
            if quantity > 0:
                return quantity
            else:
                print("Enter a whole number greater than zero.")
        except ValueError:
            print("Please enter a whole number, like 5.")


# Restocks an existing type or adds a new type with its price and quantity.
def add_equipment():
    name = input("Equipment name: ").strip().lower().replace(" ", "_")
    while name == "":
        print("The name cannot be blank.")
        name = input("Equipment name: ").strip().lower().replace(" ", "_")

    if name in equipment:
        quantity = get_quantity()
        equipment[name]["total"] += quantity
        equipment[name]["available"] += quantity
        print("Equipment quantity updated.")
    else:
        while True:
            try:
                price = float(input("Daily rental price: $"))
                if 0 < price < float("inf"):
                    break
                else:
                    print("Enter a positive, finite price.")
            except ValueError:
                print("Please enter a number, like 40.00.")

        quantity = get_quantity()
        equipment[name] = {
            "price": price,
            "total": quantity,
            "available": quantity
        }
        print("New equipment added.")


# Repeats the menu until the user chooses Save and exit.
def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            view_equipment()
        elif choice == "2":
            add_equipment()
        elif choice in ["3", "4", "5", "6"]:
            print("Coming soon")
        elif choice == "7":
            print("CSV saving comes next week. Changes will not be saved yet.")
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 7.")


main()
