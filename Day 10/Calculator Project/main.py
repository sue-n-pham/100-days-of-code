from email.charset import add_alias
from art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


n1 = ""

while True:
    if n1 == "":
        print(logo)
        try:
            n1 = float(input("What's the first number?: "))
        except ValueError:
            print("Syntax ERROR. Type in the right thing next time, dummy.")
            quit()

    for symbol in operators:
        print(symbol)
    operation = input("Pick an operation: ")
    if operation != "+" and operation != "-" and operation != "*" and operation != "/":
        print("Syntax ERROR. Type in the right thing next time, dummy.")
        quit()

    try:
        n2 = float(input("What's the next number?: "))
    except ValueError:
        print("Syntax ERROR. Type in the right thing next time, dummy.")
        quit()

    answer = operators[operation](n1, n2)
    print(f"{n1} {operation} {n2} = {answer}")

    ask = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
    if ask == "y":
        n1 = answer
    else:
        n1 = ""
        print("\n" * 100)