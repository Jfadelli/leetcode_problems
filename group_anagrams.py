def group_anagrams(strs):
    sorted_words = []
    grouped_words = []
    for i in strs:
        sorted_words.append(sorted(i))
    pointer = 0
    for i in sorted_words:
        print(i)
        for j in i:
            print(j)
        

    return sorted_words

testcase = ["eat","tea","tan","ate","nat","bat"]
testcasecans = [["bat"],["nat","tan"],["ate","eat","tea"]]

print(group_anagrams(testcase))
print(testcasecans)