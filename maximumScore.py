def maximumScore(nums,multipliers):
    nums_start = ""
    def checkStartPoint(nums, multipliers):
        if nums[0] * multipliers[0] > nums[-1] * multipliers[0]:
            nums_start = "beg"
        else: 
            nums_start = "end"
        return nums_start

    nums_start = checkStartPoint(nums, multipliers)
    m = len(multipliers)-1
    if nums_start == "end": 
        i,j,total = len(nums)-1,0,0
        while m >= 0:
            total += nums[i] * multipliers[j]
            i -= 1
            j += 1
            m -= 1
            print(total)
    else:
        i,j,total = 0,0,0
        while i <= m:
            add = nums[i] * multipliers[j]
            total += add
            i += 1
            j += 1
            print(total)

    return total
        

    


nums = [-5,-3,-3,-2,7,1]

mult = [-10,-5,3,4,6]
print(maximumScore(nums, mult))