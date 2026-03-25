def inventory_manager():
    inventory = {}

    while True:
        print("\nOptions: [1] Add [2] Remove [3] List [4] Exit")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            item_name = input("Enter item name: ").strip().capitalize()
            try:
                qty = int(input(f"How many {item_name}s? "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            inventory[item_name] = inventory.get(item_name, 0) + qty
            print(f"Updated: {item_name} (Total: {inventory[item_name]})")

        elif choice == '2':
            item_name = input("Enter item name to remove: ").strip().capitalize()
            if item_name in inventory:
                del inventory[item_name]
                print(f"{item_name} removed from inventory.")
            else:
                print(f"{item_name} not found in inventory.")

        elif choice == '3':
            if not inventory:
                print("Inventory is empty.")
            else:
                print("--- Current Inventory ---")
                for item, quantity in inventory.items():
                    print(f"- {item}: {quantity}")

        elif choice == '4':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

inventory_manager()