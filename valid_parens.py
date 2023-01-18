def isValid(s):
    valid_chars = {'(':')','{':'}','[':']'}
    stack = []
    for char in s:
        if len(stack) == 0:
            stack.append(char)
        if not stack or stack[-1] != valid_chars[char]:
            return False
        stack.pop()
    return not stack

testcase="()[]{}"
print(isValid(testcase))