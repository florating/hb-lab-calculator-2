"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


myops_1arg = {
    "square":square,
    "cube":cube
}


myops_2args = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
    "pow":power,
    "mod":mod
}


def calculate(input_tokens):
    """Checks for beginning operator, then calls corresponding arithmetic function"""
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

"""
GOAL: re-implement the REPL in calculator.py (from calculator-1 lab) from scratch.
FUNCTIONS:
    encapsulated environment that allows the user to:
        LOOP: 
            input individual arithmetic strings
                check if input is the quit string
                    close the program

                # formatting
                fx: tokenize the string into a list
                
                fx: identify which operation to perform
                    EG: 'pow' ---> power()
                    fx calls from arithemtic.py: evaluate the expression

            quit the program with a specific string
"""

def main():
    """Accepts user input in format of 'operator number number'
    and performs calculation. Type q to quit.
    """
    while True:
        print("What would you like to calculate? \
        \nEG: 'pow 3 5' will calculate 3 to the power of 5")
        # assumed to fit our format, might validate later
        user_input = input("> ")          # 'pow 3 5'
        tokens = tokenize(user_input)    # tokens = ['pow', 3, 5]
        if type(tokens) == str:
            print("This expression is invalid. Try again.")
            continue
            # check if tokens is valid (integer check)
        elif tokens[0] == 'q' or tokens[0] == 'quit':
            print("Okay, goodbye!") # exit statement
            return  # exit the calculator
        else:
            print(calculate(tokens))

main()