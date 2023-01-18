def strStr(haystack, needle):
    if not needle:
        return 0
    elif needle not in haystack:
        return -1
    tmp_str = ""
    while haystack:
        for i in haystack:
            tmp_str += i
            if needle in tmp_str:
                return len(tmp_str)-len(needle)

data1 = "aaa"
data2 = "aa"

print(f'needle found at: {strStr(data1,data2)}\nneedle location: {data2}')