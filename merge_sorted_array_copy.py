from re import I


def merge(nums1, m, nums2, n):
    p1, p2 = m-1, n-1

    for p in range(n+m -1, -1, -1):
        if p2 < 0:
            break
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
    return nums1





data= {
    "nums1":[-1,0,0,0,3,0,0,0,0,0,0],
    "m":5,
    "nums2":[-1,-1,0,0,1,2],
    "n":3
}

print(merge(data["nums1"],data["m"],data["nums2"],data["n"]))