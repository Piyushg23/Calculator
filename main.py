# Simple calculator: add, subtract, multiply, divide

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: cannot divide by zero"
    return x / y


def main():
    operations = {
        "1": ("Add", add),
        "2": ("Subtract", subtract),
        "3": ("Multiply", multiply),
        "4": ("Divide", divide),
    }
    while True:
        print("\nSimple Calculator")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        if choice not in operations:
            print("Invalid choice, try again.")
            continue
        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue
        name, func = operations[choice]
        print(f"{name} result: {func(x, y)}")


if __name__ == "__main__":
    main()
