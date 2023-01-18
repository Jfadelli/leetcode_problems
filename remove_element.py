def removeElement(nums,val):
    print(nums, val)
    pointer = len(nums)-1
    while pointer <= len(nums) and pointer >= 0:
        print(f'curr idx: {pointer}')
        if nums[pointer] == val:
            nums.remove(val)
        pointer -= 1
    ans = len(nums)
    print(nums)
    return ans

data_nums = [0,1,2,2,3,0,4,2]
data_val = 2

print(removeElement(data_nums,data_val))