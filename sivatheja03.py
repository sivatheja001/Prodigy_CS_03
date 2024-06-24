import re

password_rules = {
    'min_length': "Your password doesn't have at least 8 characters.",
    'special_char': "Your password doesn't have any special characters.",
    'uppercase': "Your password doesn't have any uppercase letter.",
    'lowercase': "Your password doesn't have any lowercase letter.",
    'digit': "Your password doesn't have any numerical digits."
}

def check_password_strength(password):
    strength = 0

    # Rule: Minimum length of 8 characters
    if len(password) >= 8:
        print("✓ Minimum length of 8 characters.")
        strength += 1
    else:
        print(f"✗ {password_rules['min_length']}")

    # Rule: Contains at least one special character
    if re.search(r'[\W_]', password):
        print("✓ Contains at least one special character.")
        strength += 1
    else:
        print(f"✗ {password_rules['special_char']}")

    # Rule: Contains at least one uppercase letter
    if re.search(r'[A-Z]', password):
        print("✓ Contains at least one uppercase letter.")
        strength += 1
    else:
        print(f"✗ {password_rules['uppercase']}")

    # Rule: Contains at least one lowercase letter
    if re.search(r'[a-z]', password):
        print("✓ Contains at least one lowercase letter.")
        strength += 1
    else:
        print(f"✗ {password_rules['lowercase']}")

    # Rule: Contains at least one numerical digit
    if re.search(r'[0-9]', password):
        print("✓ Contains at least one numerical digit.")
        strength += 1
    else:
        print(f"✗ {password_rules['digit']}")

    print(f"\nPassword strength: {strength}/5")

if __name__ == "__main__":
    user_password = input("Enter your password: ")
    check_password_strength(user_password)
