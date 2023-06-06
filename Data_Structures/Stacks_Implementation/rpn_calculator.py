import Stacks_Implementation as s
import math

rpn_stack = s.Stack()

equation = '2 1 49 2 √ + * 4 /'
equation = equation.split()

for item in equation:
    if item.isdigit():
        rpn_stack.push(int(item))

    elif item == "+":
        n1 = rpn_stack.pop()
        n2 = rpn_stack.pop()

        rpn_stack.push(n1 + n2)

    elif item == "*":
        n1 = rpn_stack.pop()
        n2 = rpn_stack.pop()

        rpn_stack.push(n1 * n2)

    elif item == "-":
        n1 = rpn_stack.pop()
        n2 = rpn_stack.pop()

        rpn_stack.push(n2 - n1)

    elif item == "/":
        n1 = rpn_stack.pop()
        n2 = rpn_stack.pop()

        rpn_stack.push(n2 / n1)

    elif item == "^":
        n1 = rpn_stack.pop()
        n2 = rpn_stack.pop()

        rpn_stack.push(n2 ** n1)

    elif item == "√":
        n1 = rpn_stack.pop()
        n2 = rpn_stack.pop()

        rpn_stack.push(n2 ** (1/n1))

answer = rpn_stack.pop()
if rpn_stack.empty():
    print(f"Answer is {answer}")
else:
    print("Error Occurred")