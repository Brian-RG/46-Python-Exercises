def pangram(sentence,abecedary):
    common=[]
    for c in sentence:
        if c in common:
            pass
        elif c in abecedary:
            common.append(c)
    a=len(common)
    b=len(abecedary)
    print (a)
    print(b)
    if a==b:
        print("The sentence is a pangram")
    else:
        print("is not a pangram")
abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
print("This program will check if any sentence you enter is a pangram")
sen=input("Please, introduce your sentence: ")
pangram(sen,abc)
