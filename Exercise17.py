def is_Palindrome(text):
    new=""
    compare=""
    non_acceptable=[" ",",",", ",".","''","'"]
    for c in text:
        if c in non_acceptable:
            pass
        else:
            compare+=c
    v=len(text)
    while v>0:
        v-=1
        if text[v] in non_acceptable:
            pass
        else:
            new+=text[v]
    if new==compare:
        print("The text is a palindrom")
    else :
        print(text)
        print(new)
        print("the text is not a palindrom")

rev=input("Please, introduce a text: ")

is_Palindrome(rev)
