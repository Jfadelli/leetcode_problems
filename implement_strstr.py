def strStr(haystack, needle):
    if needle not in haystack:
        return -1
    needle_position = 0
    while haystack:
        if needle in haystack:
            haystack = haystack[1:]
            
            needle_position += 1
        else: 
            return needle_position -1
    return needle_position -1

data1 = "abc"
data2 = "c"

print(f'needle found at: {strStr(data1,data2)}\nneedle location: {data2}')