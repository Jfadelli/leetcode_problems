def isValid(s):
    print('run')
    chars = dict({"(":")","[":"]","{":"}"})
    print(chars)
    for i in s:
        if i in chars:
            pass
        else: return False
    return True


data = "(){{}}"
print(isValid(data))