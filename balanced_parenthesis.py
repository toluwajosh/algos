"""balanced parenthesis problem
check whether or not a string
has balanced usage of parenthesis.
Example:
    (), ()(), (({[]}))  <- Balanced.
    ((), {{{)}], [][]]] <- Not Balanced.

we will implement using a list's append and pop
"""

opening_dict = {"(": ")", "[": "]", "{": "}"}
closing_dict = {")": "(", "]": "[", "}": "{"}


def isBalanced(string):
    stack = []
    for s in string:
        if s in opening_dict:
            print("opening: ", s)
            stack.append(opening_dict[s])
        elif s in closing_dict:
            print("closing: ", s)
            if len(stack) == 0:
                return False
            if s != stack.pop():
                return False
    return True


if __name__ == "__main__":
    print(isBalanced("(), ()(), (({[]}))"))
    print(isBalanced("((), {{{)}], [][]]]"))
    print(isBalanced("(((({}))))"))
    print(isBalanced("[][]]]"))
    print(isBalanced("[][]"))
