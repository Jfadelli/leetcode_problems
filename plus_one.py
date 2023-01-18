def plusOne(digits):
    pointer = len(digits)-1    
    while pointer >= 0:        
        tmp = digits[pointer]     
        if tmp == 9:
            digits[pointer] = 0
            pointer -= 1
            if pointer == -1:
                digits.insert(0,1)
        else:
            digits[pointer] += 1
            return digits
    return digits

digits = [1,2,3]

print(f'test case: {digits}\nresult: {plusOne(digits)}')