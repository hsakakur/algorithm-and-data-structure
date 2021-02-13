import sys

rp_input = input().split(" ")

stack = []

def is_num(s):
    try:
        float(s)
    except ValueError:
        return False
    else:
        return True

for character in rp_input:
    print(stack)
    if is_num(character):
        stack.append(character)
    else:
        numeric1 = stack.pop()
        numeric2 = stack.pop()
        if not is_num(numeric1):
            print('The input is incorrect as Reverse Polish Notation. ' + numeric1 + ' is not numeric.', sys.stderr)
        if not is_num(numeric2):
            print('The input is incorrect as Reverse Polish Notation. ' + numeric2 + ' is not numeric.', sys.stderr)

        numeric1 = int(numeric1)
        numeric2 = int(numeric2)

        if character == '+':
            stack.append(str(numeric2 + numeric1))
        elif character == '-':
            stack.append(str(numeric2 - numeric1))
        elif character == '*':
            stack.append(str(numeric2 * numeric1))
        elif character == '/':
            stack.append(str(numeric2 / numeric1))
        else:
            print('The input is incorrect as Reverse Polish Notation. ' + character + ' is not operand.', sys.stderr)

result = stack.pop()
if len(stack) != 0:
    print('Calculation in Reverse Polish Notation is incorrect', sys.stderr)

print(result)