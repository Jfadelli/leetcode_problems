def lengthOfLastWord(s):
    words = []
    tmp_words = reversed(s.split(" "))
    for i in tmp_words:

        if len(i) != 0:
            words.append(i)    
    return len(words[-1])

string = "   fly me   to   the moon  "

print(lengthOfLastWord(string))