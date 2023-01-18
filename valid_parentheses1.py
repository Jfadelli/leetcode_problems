def isValid(s):
    class List_of_chars():
        def __init__(self, parens, squares, curlies ):
            self.parens = parens
            self.squares = squares
            self.curlies = curlies
    #check for pairs, if ( +1 to parens if ) -1 to parens

    chars = List_of_chars( [], [], [])
    
    for i in s:
        if i == "(":
            chars.parens.append("(")
        if i == "[":
            chars.squares.append("[")
        if i == "{":
            chars.curlies.append("{")
        if (i == ")") & (len(chars.parens) != 0):
            chars.parens.pop()
        if (i == "]") & (len(chars.squares) != 0):
            chars.squares.pop()
        if (i == "}") & (len(chars.curlies) != 0):
            chars.curlies.pop()

    ans = (len(chars.parens)) + (len(chars.squares)) + (len(chars.curlies))

    if  ans > 0:
        return False
    else: 
        return True

data = "(){{[}}]"
print(isValid(data))