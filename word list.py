# function to check weather
#first and last letter of the word is same or not
def match_words(words):
    ctr = 0
    lst=[]
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("Words with matching first and last letters same\n:", lst)
    return ctr
count = match_words(['abc', 'xyz', 'aba', '1221'])
print("Number of words with matching first and last letters same:", count)