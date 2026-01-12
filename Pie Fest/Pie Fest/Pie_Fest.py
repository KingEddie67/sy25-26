lineup = [
    ("Syntax Error", "Metal", 60),
    ("The Pythonistas", "Rock", 45),
    ("Code Play", "Indie", 30),
]

while True:
    print("\n--- PyFest 2026 Stage Manager ---")
    print("1. View Lineup")
    print("2. Add Band")
    print("3. Move First Band to End (Late Arrival)")
    print("4. Remove a Band by Name")
    print("5. Exit")

    choice = input("Select an option (1-5): ")

    if choice == "1":
        print("\n--- Current Lineup ---")
        total_time = 0
        for i, (name, genre, duration) in enumerate(lineup, 1):
            print(f"{i}. {name} ({genre}) - {duration} mins")
            total_time += duration
        print(f"\nTotal Festival Duration: {total_time} minutes")
    elif choice == "2":
        name = input("Enter band name: ")
        genre = input("Enter genre: ")
        while True:
            try:
                duration = int(input("Enter performance duration (in minutes): "))
                break
            except ValueError:
                print("Please enter a valid number for duration.")

        lineup.append((name, genre, duration))
        print(f"{name} has been added to the lineup.")

    elif choice == "3":
        if len(lineup) > 1:
            late_band = lineup.pop(0)
            lineup.append(late_band)
            print(f"{late_band[0]} has been moved to the end of the lineup due to late arrival.")
        else:
            print("Not enough bands to move.")

    elif choice == "4":
        band_name = input("Enter the name of the band to remove: ")
        for band in lineup:
            if band[0].lower() == band_name.lower():
                lineup.remove(band)
                print(f"{band_name} has been removed from the lineup.")
                break
        else:
            print(f"{band_name} not found in the lineup.")

    elif choice == "5":
        print("Exiting PyFest Stage Manager.")
        break
    else:
        print("Invalid option. Please select a number between 1 and 5.")