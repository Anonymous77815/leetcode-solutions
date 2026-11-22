def calculate(s):
    stack = []
    number = 0
    sign = "+"

    for i in range(len(s)):
        if s[i].isdigit():
            number = number*10 + int(s[i])

        if s[i] in '*/+-' or i == len(s)-1:

            if sign == "+":
                stack.append(number)

            elif sign == "-":
                stack.append(-number)

            elif sign == "/":
                stack.append(stack.pop()/number)

            elif sign == "*":
                stack.append(stack.pop()*number)

            sign = s[i]

            number = 0

    return sum(stack)