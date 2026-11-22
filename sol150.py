def evalRPN(tokens):

    stack = []

    for i in range(len(tokens)):

        if tokens[i] == "+" and stack:
            sum_token = stack[-1] + stack[-2]
            stack.pop()
            stack.pop()
            stack.append(sum_token)

        elif tokens[i] == "-" and stack:
            a = stack.pop()
            b = stack.pop()

            result = b - a
            stack.append(result)

        # elif tokens[i] == "/" and stack:
        #     div_token = int(stack[-2] / stack[-1])
        #     stack.pop()
        #     stack.pop()
        #     stack.append(div_token)
        

        elif tokens[i] == "/" and stack:
            a = stack.pop()   # divisor (top)
            b = stack.pop()   # dividend (second from top)
            result = abs(b) // abs(a)
            if (a < 0) != (b < 0):   # signs differ -> negative result
                result = -result
            stack.append(result)

        elif tokens[i] == "*" and stack:
            mul_token = stack[-1]*stack[-2]
            stack.pop()
            stack.pop()
            stack.append(mul_token)

        else:
            stack.append(int(tokens[i]))


    return stack[0]
            


print(evalRPN(["2","1","+","3","*"]))
print(evalRPN(["4","13","5","/","+"]))
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))