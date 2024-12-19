import json
import os

# File path for storing user data
DATA_FILE = 'data.json'

def load_data():
    """Load data from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_data(data):
    """Save data to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_or_update_user(username, tokens, badge):
    """Add a new user or update an existing user's data."""
    # Load existing data
    data = load_data()

    # Check if the user exists; if not, create an entry
    if username not in data:
        data[username] = {
            "tokens": 0,
            "badges": []
        }

    # Update user data
    data[username]["tokens"] += tokens
    if badge not in data[username]["badges"]:
        data[username]["badges"].append(badge)

    # Save updated data
    save_data(data)
    print(f"Data for user '{username}' has been updated.")

def main():
    """Main function to interact with the user."""
    print("Welcome to the User Data Manager!")

    # Get user input
    username = input("Enter username: ").strip()
    tokens = int(input("Enter tokens to add: "))
    badge = input("Enter badge to add: ").strip()

    # Add or update user
    add_or_update_user(username, tokens, badge)

if __name__ == "__main__":
    main()
