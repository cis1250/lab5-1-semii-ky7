#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
#!/usr/bin/env python3

# Fibonacci Sequence Program (Modular Version)

def ask_user_input():
    user_input = input("How many terms of the Fibonacci sequence do you want? ")
    return user_input


def validate_input(user_input):
    try:
        value = int(user_input)
        if value > 0:
            return value
        else:
            print("Please enter a positive number.")
            return None
    except:
        print("Please enter a number.")
        return None


def generate_fibonacci(n):
    a, b = 0, 1
    sequence = []
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def print_sequence(sequence):
    print("Fibonacci sequence:")
    for num in sequence:
        print(num, end=" ")
    print()


def main():
    while True:
        raw_input = ask_user_input()
        valid_number = validate_input(raw_input)
        if valid_number is not None:
            break
    fib = generate_fibonacci(valid_number)
    print_sequence(fib)


if __name__ == "__main__":
    main()
