
import secrets
import string

print("===== RANDOM PASSWORD GENERATOR =====")


def ask_yes_no(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()

        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        else:
            print("Invalid choice! Please type yes or no.")


while True:
    try:
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("Error: Password must contain at least 8 characters.")
            continue

        print("\nChoose the characters for your password:")
        print("Type yes to include or no to exclude.\n")

        upper = ask_yes_no("Include CAPITAL letters (A-Z)?")
        lower = ask_yes_no("Include small letters (a-z)?")
        numbers = ask_yes_no("Include numbers (0-9)?")
        symbols = ask_yes_no("Include special symbols (!@#$)?")

        groups = []

        if upper:
            groups.append(string.ascii_uppercase)
        if lower:
            groups.append(string.ascii_lowercase)
        if numbers:
            groups.append(string.digits)
        if symbols:
            groups.append(string.punctuation)

        if len(groups) < 2:
            print("Error: Select at least 2 character types.")
            continue

        characters = "".join(groups)

        password = [
            secrets.choice(group) for group in groups
        ]

        password += [
            secrets.choice(characters)
            for _ in range(length - len(password))
        ]

        secrets.SystemRandom().shuffle(password)

        print("\n===== YOUR PASSWORD =====")
        print("Generated Password:", "".join(password))
        print("Password Length:", length)
        print("=========================")

        again = ask_yes_no("\nDo you want to generate another password?")

        if not again:
            print("\nThank you for using Password Generator!")
            break

    except ValueError:
        print("Error: Please enter a valid whole number.")

