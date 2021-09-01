"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

"""
Now, how should we evaluate our list of tokens (['pow', '3', '5'])?
Take some time to think about this and jot down some preliminary pseudocode
before you continue to the next paragraph.

EXAMPLE:
input_string = 'pow 3 5'
tokens = input_string.split(' ')   # => ['pow', '3', '5']
"""


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
    

def tokenize(input_string):     # 'pow 3 5' vs 'square 3'
    """Take a string and return a list of its constituent parts."""
    tokens = input_string.split(' ')
    i = 1
    while i < len(tokens):
        tokens[i] = int(tokens[i])  # validate?
        i += 1
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
    """ """
    while True:
        print("What would you like to calculate? \
        \nEG: 'pow 3 5' will calculate 3 to the power of 5")
        # assumed to fit our format, might validate later
        user_input = input("")          # 'pow 3 5'

        tokens = tokenize(user_input)    # tokens = ['pow', 3, 5]
        if tokens[0] == 'q' or tokens[0] == 'quit':
            # exit statement
            return  # exit the calculator
        calculate(tokens)
