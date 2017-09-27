not_consider=[" ",",",".","!","?"]
def is_Palindrome(word):
    new=""
    compare=""
    for c in word:
        if c in not_consider:
            pass
        else:
            compare+=c
    v=len(word)
    while v>0:
        v-=1
        if word[v] in not_consider:
            pass
        else:
            new+=word[v]
    if new==compare:
        return True
    else :
        return False

rev=input("Please, introduce a word: ")

is_Palindrome(rev)
