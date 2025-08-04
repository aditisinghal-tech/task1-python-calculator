def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by zero."
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}
def calculator():
    print(r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")
    num1 = float(input("Enter first number: "))
    choice = input("Pick an operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    result = 0
    if choice in operations:
        result = operations[choice](num1, num2)
        print(f"{num1} {choice} {num2} = {result}")
    user_choice = input(f"type 'y' to continue calculating with '{result}', or type 'n' to start a new calculation, or type 'exit' to exit execution: ").lower()

    should_continue = True
    while should_continue:
        if user_choice == "y":
            choice = input("Pick an operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            if choice in operations:
                new_result = operations[choice](result, num2)
                print(f"{result} {choice} {num2} = {new_result}")
            user_choice = input(f"type 'y' to continue calculating with '{result}', or type 'n' to start a new calculation, or type 'exit' to exit execution: ").lower()
        if user_choice == "n":
            print("\n"*10)
            calculator()
        if user_choice == "exit":
            break
            
calculator()