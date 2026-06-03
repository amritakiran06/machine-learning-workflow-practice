def load_users(filepath):
    try:
        with open(filepath, 'r') as f:
            return [line.strip().split(',') for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_users(filepath, user_list):
    with open(filepath, 'w') as f:
        for user in user_list:
            f.write(",".join(user) + "\n")

def add_user(user_list, name, email):
    user_list.append([name, email])
    return user_list

def find_user(user_list, name):
    results = [u for u in user_list if u[0].lower() == name.lower()]
    return results[0] if results else None

def display_all(user_list):
    for name, email in user_list:
        print(f"{name:<15} | {email:<20}")

file_path = "users.txt"
active_users = load_users(file_path)

active_users = add_user(active_users, "amrita", "amrita@example.com")
active_users = add_user(active_users, "kiran", "kiran@example.com")
active_users = add_user(active_users, "siva", "siva@example.com")

save_users(file_path, active_users)

print("System Users:")
display_all(active_users)

search_name = "kiran"
found = find_user(active_users, search_name)
if found:
    print(f"\nSearch Result: {found[0]} can be reached at {found[1]}")
