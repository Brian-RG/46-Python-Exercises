import urllib.request
def Alternade(word):
    lista=urllib.request.urlopen("http://www.puzzlers.org/pub/wordlists/unixdict.txt")
    words=[]
    again_words=[]
    first_word=""
    alterated=""
    second_word=""
    alterated_two=""
    new=""
    a=r'\n'
    rango=len(word)
    for line in lista.readlines():
        words.append(str(line))
    c=0
    for c in range(rango):
        if c%2 ==0:
             first_word+=word[c]
        else:
            second_word+=word[c]
        c+=1
    count=1
    for z in words:
        again_words.append(new)
    slash=(r'\n')
    alterated="b'"+first_word+slash+"'"
    alterated_two="b'"+second_word+slash+"'"
    if alterated in words:
        if alterated_two in words:
            print ("'",word,"' makes '",first_word,"' and '",second_word,"'")
        else:
            print("'",word,"' makes'",first_word,"'")
    elif alterated_two in words:
        print("'",word,"' makes'",second_word,"'")
    else:
        print(new)
        print(first_word)
        print(second_word)
        print (words[90])
        print ("There are no words with those letters")

#main

print("This program will make any word you enter an alternade")
word=input("Please, enter a word: ")
Alternade(word)
