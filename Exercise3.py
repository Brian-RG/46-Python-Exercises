def Length(word):
    num=0
    for element in word:
        num+=1
    return num
word=input("Introduce a word: ")

print("The length of the word is ",Length(word))
