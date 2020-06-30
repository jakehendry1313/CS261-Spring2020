# Author:      Jacob Hendry
# Date:        04/21/2020
# Description: This is a python file called balance.py. It will determine if the input
#              string is balanced.

import sys


# Checks whether the input string is balanced
# param: input string
# returns True if the string is balanced, otherwise returns False
def is_balanced(input_string):

    # initialize an empty list as the stack
    stack = []
    left_side_closer = ["(", "{", "["]
    right_side_closer = [")", "}", "]"]

    # iterate over each character in the string
    for i in input_string:
        if i in left_side_closer:
            stack.append(i)
        elif i in right_side_closer:
            if not stack:
                return False
            element = stack.pop()
            if element == "(":
                if i != ")":
                    return False
            if element == "{":
                if i != "}":
                    return False
            if element == "[":
                if i != "]":
                    return False
    if stack:
        return False
    return True


if __name__ == '__main__':
    # get input string
    _input_string = sys.argv[1]  # DO NOT MODIFY

    balanced = is_balanced(_input_string)

    if balanced:
        print("The string {} is balanced".format(_input_string))
    else:
        print("The string {} is not balanced".format(_input_string))
