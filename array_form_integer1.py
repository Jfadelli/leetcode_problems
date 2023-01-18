def test(num,k):
    int_num = 0
    len_og_num = len(num)
    for idx, x in enumerate(num):
        mult = 1
        curr_factor = len_og_num - idx
        for i in range(curr_factor-1):
            mult = mult * 10
        int_num += (x*mult)
        sum = int_num+k
        ans = list(map(int, str(sum)))
    return(ans)

data = [9,9,9,9,9,9,9,9,9,9,9]
k = 1
print(f'test result: {test(data,k)}')
print(f'Correct res: {999999999999+1}')