# ---------------------------------------------
# MASTERMIND GAME PROJECT - LOGIN AUTHENTICATION
# ---------------------------------------------

# Sample dictionary storing registered users
registered_users = {
    "player1": "pass123",
    "player2": "mastermind",
    "admin": "nidec2025"
}

def login():
    print("=====================================")
    print("     WELCOME TO MASTERMIND GAME      ")
    print("=====================================")
    print("Please log in to continue.\n")

    # Maximum login attempts allowed
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ").strip()

        # Check if username exists and password matches
        if username in registered_users and registered_users[username] == password:
            print(f"\nLogin successful! Welcome, {username}.\n")
            return username  # Return username to use later in the game
        else:
            attempts += 1
            print(f"Invalid credentials. Attempts remaining: {max_attempts - attempts}\n")

    print("Too many failed attempts. Please try again later.")
    return None  # Exit or prevent access if login fails

current_user = login()

if current_user:
    print("Loading Mastermind Game...")
    # You can proceed to your game flowchart steps here:
    # generate_secret_code()
    # play_game(current_user)
else:
    print("Exiting program.")