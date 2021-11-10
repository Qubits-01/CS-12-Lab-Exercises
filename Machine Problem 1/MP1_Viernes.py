def main():
    eqn1 = ["(", "1", "+", "2", ")", "^", "3"]
    eqn2 = ['1', '+', '2']
    eqn3 = "A * B + C * D".split()
    eqn4 = "( A + B ) * C - ( D - E ) * ( F + G )".split()
    eqn5 = '( 7 + 8 ) / ( 3 + 2 )'.split()
    eqn6 = '2 ^ 3 ^ 2'.split()
    eqn7 = '3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3'.split()
    eqn8 = 'a + b * c ^ d ^ e - f / g * h'.split()
    eqn9 = 'a / b / c'.split()

    print(pemdas(eqn6))
    # print(infix_to_postfix_5(eqn8))


def pemdas(equation):
    # Infix to Postfix.
    if type(equation[-1]) is not list:
        def det_assoc(token):
            if token in '*/+-':
                return 1  # Represents left associativity.
            elif token == '^':
                return 0  # Represents right associativity.

        def get_precedence(token):
            if token in '^':
                return 3
            elif token in '*/':
                return 2
            elif token in '+-':
                return 1
            else:
                return 0

        operators_stack = []
        postfix_exp = []
        equation.insert(0, '(')
        equation.append(')')

        for token in equation:
            if token == '(':
                operators_stack.append(token)
            elif token not in '^*/+-()':
                postfix_exp.append(token)
            elif token in '^*/+-':
                while operators_stack[-1] in '^*/+-' \
                and ((get_precedence(operators_stack[-1]) > get_precedence(token)) \
                or (get_precedence(operators_stack[-1]) == get_precedence(token) \
                and det_assoc(operators_stack[-1]) and det_assoc(token))):
                    postfix_exp.append(operators_stack.pop())

                operators_stack.append(token)
            elif token == ')':
                while operators_stack[-1] != '(':
                    postfix_exp.append(operators_stack.pop())

                operators_stack.pop()

        postfix_exp.append([])
        return pemdas(postfix_exp)

    # Postfix evaluation.
    current_token = equation[0]
    ans = None

    if current_token not in '^*/+-':
        equation[-1].append(current_token)
    else:
        operand1 = float(equation[-1].pop())
        operand2 = float(equation[-1].pop())

        if current_token == '^':
            ans = operand2 ** operand1
        elif current_token == '*':
            ans = operand1 * operand2
        elif current_token == '/':
            ans = operand2 / operand1
        elif current_token == '+':
            ans = operand1 + operand2
        elif current_token == '-':
            ans = operand2 - operand1

        equation[-1].append(ans)

    # Base case.
    if len(equation) == 2:
        return ans

    return pemdas(equation[1:])


def infix_to_postfix_5(tokens):
    def det_assoc(token):
        if token in '*/+-':
            return 1  # Represents left associativity.
        elif token == '^':
            return 0  # Represents right associativity.

    def get_precedence(token):
        if token in '^':
            return 3
        elif token in '*/':
            return 2
        elif token in '+-':
            return 1
        else:
            return 0

    operators_stack = []
    postfix_exp = []
    tokens.insert(0, '(')
    tokens.append(')')

    for token in tokens:
        if token == '(':
            operators_stack.append(token)
        elif token not in '^*/+-()':
            postfix_exp.append(token)
        elif token in '^*/+-':
            while operators_stack[-1] in '^*/+-' \
            and ((get_precedence(operators_stack[-1]) > get_precedence(token)) \
            or (get_precedence(operators_stack[-1]) == get_precedence(token) \
            and det_assoc(operators_stack[-1]) and det_assoc(token))):
                postfix_exp.append(operators_stack.pop())
            # while (operators_stack[-1] in '^*/+-') and (
            #         ((0 if operators_stack[-1] not in '^*/+-' else precedence[operators_stack[-1]]) > (
            #                 0 if token not in '^*/+-' else precedence[token]
            #         )) or (
            #         (0 if operators_stack[-1] not in '^*/+-' else precedence[operators_stack[-1]]) == (
            #         (0 if token not in '^*/+-' else precedence[token]) and (
            #         1 if operators_stack[-1] in '*/+-' else (0 if operators_stack[-1] == '^' else None)) and (
            #         1 if token in '*/+-' else (0 if token == '^' else None)
            # ))
            # )
            # ):
            #     postfix_exp.append(operators_stack.pop())

            operators_stack.append(token)
        elif token == ')':
            while operators_stack[-1] != '(':
                postfix_exp.append(operators_stack.pop())

            operators_stack.pop()

    return postfix_exp


# def get_precedence(token):
#     if token in '^':
#         return 3
#     elif token in '*/':
#         return 2
#     elif token in '+-':
#         return 1
#     else:
#         return 0


# def det_assoc(token):
#     if token in '*/+-':
#         return 1  # Represents left associativity.
#     elif token == '^':
#         return 0  # Represents right associativity.


# def infix_to_postfix_4(tokens):
#     precedence = {
#         '^': 3,
#         '*': 2,
#         '/': 2,
#         '+': 1,
#         '-': 1,
#         '(': 0,
#         ')': 0
#     }
#
#     operators_stack = []
#     postfix_exp = []
#     tokens.insert(0, '(')
#     tokens.append(')')
#
#     for token in tokens:
#         if token == '(':
#             operators_stack.append(token)
#         elif (token not in precedence) and (token != ')'):
#             postfix_exp.append(token)
#         elif token in '^*/+-':
#             while (operators_stack[-1] in '^*/+-') \
#                 and (((0 if token.isdigit() else precedence[operators_stack[-1]]) > (0 if token.isdigit() else precedence[token])) \
#                     or ((0 if token.isdigit() else precedence[operators_stack[-1]]) == ((0 if token.isdigit() else precedence[token]) \
#                         and (0 if operators_stack[-1] == '^' else 1) \
#                         and (0 if token == '^' else 1)))):
#                 postfix_exp.append(operators_stack.pop())
#
#             operators_stack.append(token)
#         elif token == ')':
#             while operators_stack[-1] != '(':
#                 postfix_exp.append(operators_stack.pop())
#
#             operators_stack.pop()
#
#     return postfix_exp


# Not properly working on nested exponents (should be right associative).
# def infix_to_postfix_3(tokens):
#     operators = {'(', ')', '^', '*', '/', '+', '-'}
#     precedence = {
#         '^': 3,
#         '*': 2,
#         '/': 2,
#         '+': 1,
#         '-': 1
#     }
#
#     temp_stack = []
#     output = ''
#
#     for token in tokens:
#         if token not in operators:
#             output += token
#         elif token == '(':
#             temp_stack.append('(')
#         elif token == ')':
#             while temp_stack and temp_stack[-1] != '(':
#                 output += temp_stack.pop()
#
#             temp_stack.pop()
#         else:
#             while \
#             temp_stack \
#             and temp_stack[-1] != '(' \
#             and precedence[token] <= precedence[temp_stack[-1]]:
#                 output += temp_stack.pop()
#
#             temp_stack.append(token)
#
#     while temp_stack:
#         output += temp_stack.pop()
#
#     return output


# Not properly working on nested exponents (should be right associative).
# def infix_to_postfix_2(tokens):
#     precedence = {
#         '^': 4,
#         '*': 3,
#         '/': 3,
#         '+': 2,
#         '-': 2,
#         '(': 1
#     }
#
#     infix_tokens = tokens
#     postfix_tokens = []
#
#     temp_stack = []
#     temp_stack.append('(')
#     infix_tokens.append(')')
#
#     while infix_tokens:
#         token = infix_tokens.pop(0)
#
#         if token == '(':
#             temp_stack.insert(0, token)
#         elif token == ')':
#             while temp_stack[0] != '(':
#                 postfix_tokens.append(temp_stack.pop(0))
#
#             temp_stack.pop(0)
#         elif token in '^*/+-':
#             while temp_stack and precedence[temp_stack[0]] >= precedence[token]:
#                 postfix_tokens.append(temp_stack.pop(0))
#
#             temp_stack.insert(0, token)
#         else:
#             postfix_tokens.append(token)
#
#     return postfix_tokens


# Not properly working on nested exponents (should be right associative).
# def infix_to_postfix_1(tokens):
#     prec = {
#         '^': 4,
#         '*': 3,
#         '/': 3,
#         '+': 2,
#         '-': 2,
#         '(': 1
#     }
#     opStack = []
#     postfixList = []
#
#     for token in tokens:
#         if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
#             postfixList.append(token)
#         elif token == '(':
#             opStack.append(token)
#         elif token == ')':
#             topToken = opStack.pop()
#             while topToken != '(':
#                 postfixList.append(topToken)
#                 topToken = opStack.pop()
#         else:
#             while (not len(opStack) == 0) and \
#                (prec[opStack[-1]] >= prec[token]):
#                   postfixList.append(opStack.pop())
#             opStack.append(token)
#
#     while not len(opStack) == 0:
#         postfixList.append(opStack.pop())
#
#     return " ".join(postfixList)

# I will use this one in the pemdas function above.
def eval_postfix_2(postfix_tokens):
    if type(postfix_tokens[-1]) is not list:
        postfix_tokens.append([])
        return eval_postfix_2(postfix_tokens)

    current_token = postfix_tokens[0]
    ans = None

    if current_token not in '^*/+-':
        postfix_tokens[-1].append(current_token)
    else:
        operand1 = float(postfix_tokens[-1].pop())
        operand2 = float(postfix_tokens[-1].pop())

        if current_token == '^':
            ans = operand2 ** operand1
        elif current_token == '*':
            ans = operand1 * operand2
        elif current_token == '/':
            ans = operand2 / operand1
        elif current_token == '+':
            ans = operand1 + operand2
        elif current_token == '-':
            ans = operand2 - operand1

        postfix_tokens[-1].append(ans)

    # Base case.
    if len(postfix_tokens) == 2:
        return ans

    return eval_postfix_2(postfix_tokens[1:])


# def eval_postfix_1(tokens):
#     operandStack = []
#
#     for token in tokens:
#         if token in "0123456789":
#             operandStack.append(int(token))
#         else:
#             operand2 = operandStack.pop()
#             operand1 = operandStack.pop()
#             result = doMath(token, operand1, operand2)
#             operandStack.append(result)
#
#     return operandStack.pop()
#
#
# def doMath(op, op1, op2):
#     if op == '^':
#         return op1 ** op2
#     elif op == "*":
#         return op1 * op2
#     elif op == "/":
#         return op1 / op2
#     elif op == "+":
#         return op1 + op2
#     else:
#         return op1 - op2


# def pemdas(eqn):
#     # Base cases.
#     eqn_len = len(eqn)
#
#     if eqn_len == 1:
#         return float(eqn[0])
#
#     if eqn_len == 3:
#         if '*' in eqn:
#             return pemdas([str(float(eqn[0]) * float(eqn[-1]))])
#         elif '/' in eqn:
#             return pemdas([str(float(eqn[0]) / float(eqn[-1]))])
#         elif '+' in eqn:
#             return pemdas([str(float(eqn[0]) + float(eqn[-1]))])
#         elif '-' in eqn:
#             return pemdas([str(float(eqn[0]) - float(eqn[-1]))])


if __name__ == '__main__':
    main()
