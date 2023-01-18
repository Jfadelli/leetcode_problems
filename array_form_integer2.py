def test(num, k):
    pointer = len(num)-1
    carry_flag = 0
    while pointer >= 0 or k > 0:
        if pointer == -1:
            if k > 0:
                num.insert(0,0)
                pointer += 1
        if carry_flag > 0:
            curr_sum = k % 10 + carry_flag
        else:
            curr_sum = k % 10
        if curr_sum + num[pointer] < 10:
            num[pointer] += curr_sum
            carry_flag = 0
        else:
            new_add = curr_sum+num[pointer] - 10
            num[pointer] = new_add
            carry_flag = 1
        k = k//10
        pointer -=1
    if carry_flag:
        num.insert(0,1)
    return num

data = [0]
k = 23
print(f'test result: {test(data,k)}')
print(f'res should be, {9999999999+1}')