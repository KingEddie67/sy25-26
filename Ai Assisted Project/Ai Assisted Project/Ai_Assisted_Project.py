high_scores = {}

try:
    with open("highscores.txt", "r") as file:
        for line in file.readlines():
            parts = line.strip().split()
            if len(parts) == 2:
                high_scores[parts[0]] = int(parts[1])
except FileNotFoundError:
    pass

while True:
    if high_scores:  
        print("\n" + "*" * 32)  
        print("*   TOP 5 LEADERBOARD         *")  
        print("*" + "-" * 30 + "*")  
        sorted_leaderboard = sorted(high_scores.items(), key=lambda item: item[1], reverse=True)  
        for rank, (user, score) in enumerate(sorted_leaderboard[:5], start=1):  
            print(f"* {rank}. {user:10} : {score:4} pts      *")  
        print("*" + "-" * 30 + "*")  
        print("*" * 32)  
    else:  
        print("\nLeaderboard is currently empty.")  

    print("\n--- Menu ---")
    choice = input("Enter username, 'delete', or 'quit': ").strip()
    
    if choice.lower() == 'quit':
        break
        
    elif choice.lower() == 'delete':
        user_to_del = input("Which username should be removed? ").strip()
        if user_to_del in high_scores:
            del high_scores[user_to_del]
            with open("highscores.txt", "w") as file:
                for user, score in high_scores.items():
                    file.write(f"{user} {score}\n")
            print(f"Removed {user_to_del}.")
        else:
            print(f"Error: {user_to_del} not found.")
        continue

    name = choice
    try:
        new_score = int(input(f"Enter score for {name}: "))
    except ValueError:
        print("Error: Please enter a whole number.")
        continue

    if name not in high_scores or new_score > high_scores[name]:
        high_scores[name] = new_score
        print(f"Success! {name}'s high score is now {new_score}.")
    else:
        print(f"No update. {name}'s best remains {high_scores[name]}.")

    with open("highscores.txt", "w") as file:
        for user, score in high_scores.items():
            file.write(f"{user} {score}\n")

print("\nFinal scores saved. Goodbye!")
