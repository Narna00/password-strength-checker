import re
import getpass
import random
import string

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]

    if all(not error for error in errors):
        return "Strong"
    elif sum(errors) == 1:
        return "Medium"
    else:
        return "Weak"

def suggest_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(12))
    return password

def main():
    print("=== Password Strength Checker ===")
    password = getpass.getpass("Enter your password: ")
    strength = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")

    if strength == "Strong":
        print("✅ Great! Your password is strong.")
        return

    # Give improvement tips
    print("\n⚙️ Tips to improve your password:")
    if len(password) < 8:
        print("- Make it at least 8 characters long.")
    if re.search(r"\d", password) is None:
        print("- Add at least one number.")
    if re.search(r"[A-Z]", password) is None:
        print("- Add at least one uppercase letter.")
    if re.search(r"[a-z]", password) is None:
        print("- Add at least one lowercase letter.")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None:
        print("- Add at least one special character (e.g., !, @, #, $).")

    # Offer to generate a strong password
    choice = input("\nWould you like me to generate a strong password for you? (yes/no): ").lower()
    if choice == 'yes':
        new_password = suggest_password()
        print(f"\n🔑 Suggested Strong Password: {new_password}")
    else:
        print("\nThank you for using the Password Strength Checker!")

if __name__ == "__main__":
    main()
