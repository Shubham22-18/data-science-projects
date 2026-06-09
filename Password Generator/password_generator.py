import random
import string

def generate_password(length):
    characters = (
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        string.punctuation
    )

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:
    print("\n===== Password Generator =====")
    print("1. Generate Password")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password length should be at least 4.")
        else:
            password = generate_password(length)
            print("\nGenerated Password:")
            print(password)

    elif choice == "2":
        print("Exiting Password Generator...")
        break

    else:
        print("Invalid choice!")
