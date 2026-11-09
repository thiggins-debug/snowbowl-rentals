# Teddy Higgins
# SnowBowl Montana Rental Shop - Week 2
# These are sample prices and quantities, not actual SnowBowl data.
# Data is only stored while the program is running this week.

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


# Repeats the menu until the user chooses Save and exit.
def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "7":
            print("CSV saving comes next week. Changes will not be saved yet.")
            print("Goodbye!")
            break
        elif choice in ["1", "2", "3", "4", "5", "6"]:
            print("Coming soon")
        else:
            print("Invalid option. Please choose a number from 1 to 7.")


main()
