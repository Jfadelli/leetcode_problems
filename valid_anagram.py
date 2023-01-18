def isAnagram(s,t):
    stack = list(s)
    stack2 = list(t)
    idx = 0
    while idx < len(stack):
        if stack[idx] in stack2:
            stack2.remove(stack[idx])
            idx += 1
        else: 
            return False
    if len(stack2) == 0: 
        return True
    else: 
        return False
        

    


s = "rat" 
t = "car"
print(isAnagram(s,t))