def calPoints(operations):
    stack = []
    output = 0
    for i in operations:
        try:
            test_string = int(i)
            stack.append(test_string)
        except:
            if i == "+":
                stack.append(stack[-1]+stack[-2])
            if i == "D":
                stack.append(stack[-1]*2)
            if i == "C":
                stack.pop()
    for i in stack:
        output += i
    return output

input = ["5","-2","4","C","D","9","+","+"]
print(calPoints(input))