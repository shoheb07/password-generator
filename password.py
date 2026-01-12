import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== PASSWORD GENERATOR ===")

    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Invalid length.")
        return

    use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
    use_digits = input("Include numbers? (y/n): ").lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").lower() == "y"

    password = generate_password(
        length, use_upper, use_lower, use_digits, use_symbols
    )

    if password:
        print("\nGenerated Password:", password)
    else:
        print("No character set selected.")

if __name__ == "__main__":
    main()
