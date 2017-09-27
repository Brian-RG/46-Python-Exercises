def Vowel(x):
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        return True
    else:
        return False

#main
let=input("Introduce a character: ")
print(Vowel(let))
