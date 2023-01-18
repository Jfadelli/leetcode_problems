from re import I


def merge(nums1, m, nums2, n):
    idx = 0
    while nums2:
        curr, next = nums1[idx],nums2[0]
        if next > curr:
            nums1.insert(idx+1, next)
            nums1.pop()
            nums2 = nums2[1:]
            idx += 2
        elif next < curr:
            nums1.pop()
            idx += 1
        elif next == curr:
            nums1.insert(idx, next)
            nums1.pop()
            nums2 = nums2[1:]
            idx += 1

    return nums1

data= {
    "nums1":[-1,0,0,0,3,0,0,0,0,0,0],
    "m":5,
    "nums2":[-1,-1,0,0,1,2],
    "n":3
}

print(merge(data["nums1"],data["m"],data["nums2"],data["n"]))