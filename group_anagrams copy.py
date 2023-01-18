def group_anagrams(strs):
    char_to_bin = {
    "a" : 0b10000000000000000000000000,
    "b" : 0b01000000000000000000000000,
    "c" : 0b00100000000000000000000000,
    "d" : 0b00010000000000000000000000,
    "e" : 0b00001000000000000000000000,
    "f" : 0b00000100000000000000000000,
    "g" : 0b00000010000000000000000000,
    "h" : 0b00000001000000000000000000,
    "i" : 0b00000000100000000000000000,
    "j" : 0b00000000010000000000000000,
    "k" : 0b00000000001000000000000000,
    "l" : 0b00000000000100000000000000,
    "m" : 0b00000000000010000000000000,
    "n" : 0b00000000000001000000000000,
    "o" : 0b00000000000000100000000000, 
    "p" : 0b00000000000000010000000000,
    "q" : 0b00000000000000001000000000,
    "r" : 0b00000000000000000100000000,
    "s" : 0b00000000000000000010000000,
    "t" : 0b00000000000000000001000000,
    "u" : 0b00000000000000000000100000,
    "v" : 0b00000000000000000000010000,
    "w" : 0b00000000000000000000001000,
    "x" : 0b00000000000000000000000100,
    "y" : 0b00000000000000000000000010,
    "z" : 0b00000000000000000000000001,
    }
    bin_words = []
    ans = []
    for i in strs:
        curr_word = 0b00000000000000000000000000
        for j in i:
            curr_word = curr_word + char_to_bin.get(j)
        print(bin(curr_word))
        bin_words.append(curr_word)
    p1 = 0
    while p1 < len(bin_words):
        p2 = p1+1
        curr_list = []
        curr_word = bin(bin_words[p1])
        while p2 < len(bin_words):
            next_word = bin(bin_words[p2])
            if curr_word == next_word:
                curr_list.append(strs[p2])
            p2 += 1
        ans.append(curr_list)
        p1 += 1

    return ans

testcase = ["eat","tea","tan","ate","nat","bat"]
testcasecans = [["bat"],["nat","tan"],["ate","eat","tea"]]


print(group_anagrams(testcase))
print(testcasecans)