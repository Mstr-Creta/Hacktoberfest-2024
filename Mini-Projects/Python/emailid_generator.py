def generate_email_combinations(first_name, last_name, domain):
   
    combinations = [
        f"{first_name}.{last_name}@{domain}",
        f"{first_name}_{last_name}@{domain}",
        f"{first_name}{last_name}@{domain}",
        f"{first_name[0]}{last_name}@{domain}",
        f"{first_name}{last_name[0]}@{domain}",
        f"{last_name}.{first_name}@{domain}",
        f"{last_name}_{first_name}@{domain}",
        f"{last_name}{first_name}@{domain}"
    ]
    
    return combinations

def choose_email(combinations):
   
    print("Here are the possible email combinations:")
    for i, email in enumerate(combinations, 1):
        print(f"{i}. {email}")
    
    
    choice = int(input("Enter the number of the email you prefer: "))
    if 1 <= choice <= len(combinations):
        return combinations[choice - 1]
    else:
        print("Invalid choice, please try again.")
        return choose_email(combinations)


first_name = input("Enter your first name: ").lower()
last_name = input("Enter your last name: ").lower()
domain = input("Enter the email domain (e.g., gmail.com, outlook.com): ").lower()


email_combinations = generate_email_combinations(first_name, last_name, domain)
selected_email = choose_email(email_combinations)

print(f"Your selected email is: {selected_email}")
