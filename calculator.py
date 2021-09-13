"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

myops_1arg = {
    "square": square,
    "cube": cube
}

myops_2args = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "pow": power,
    "mod": mod
}


def calculate(input_tokens):
    """Return calculation after checking for operator at index 0 and calling the corresponding arithmetic function.
    
    INPUT: tokenized string --> ['pow', 3, 5]
    OUTPUT: calculation --> 3 to the power of 5 --> 243

    If this is not a valid expression, the function will return an error message.
    """
    op = input_tokens[0]
    if op in myops_1arg:
        oplist = myops_1arg
        operation = oplist[op]
        return operation(input_tokens[1])
    elif op in myops_2args:
        oplist = myops_2args
        operation = oplist[op]
        return operation(input_tokens[1], input_tokens[2])
    return "This is not a valid expression."
    

def tokenize(input_string):     # 'pow 3 5' vs 'square 3'
    """Take a string and return a list of its constituent parts."""
    tokens = input_string.split(' ')
    i = 1
    while i < len(tokens):
        try:
            tokens[i] = int(tokens[i])  # validate? using try-except
            i += 1
        except ValueError:
            return 'error'
    return tokens


def main():
    """Opens up the REPL calculator interface within the Python interpreter.
    
    Accepts user input in string format of 'operator number number'
    and performs calculation.
    
    Type q to quit.
    """
    while True:
        print("What would you like to calculate?")
        # assumed to fit our format, might validate later
        user_input = input("> ")        # 'pow 3 5'
        tokens = tokenize(user_input)   # tokens = ['pow', 3, 5]
        if type(tokens) == str:
            print("This expression is invalid. Try again.")
            continue
            # check if tokens is valid (integer check)
        elif tokens[0] in ('q', 'quit'):
            print("Okay, goodbye!")     # exit statement
            return                      # exit the calculator
        elif tokens[0] in ('?', 'help', 'options'):
            show_help_options()
        else:
            print(calculate(tokens))


def show_help_options():
    """Show options via help menu."""
    print("This is a prefix calculator. It will evaluate expressions \
        \n in the format of 'operator operand1 operand2' and evaluate \
        \n in the format of: operand1 operator operand2. \
        \n\nEG: 'pow 3 5' will calculate 3 to the power of 5")
    print("\nFunctions that take 1 argument include:")
    for key, value in myops_1arg.items():
        print("{:<10}".format(key), value.__name__)
    print("\nFunctions that take 2 arguments include:")
    for key, value in myops_2args.items():
        print("{:<10}".format(key), value.__name__)
    print("\nType 'q' or 'quit' to exit the program.\n")

main()
